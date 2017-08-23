from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from alumnos.models import DatosPersonales
from django.core.mail import send_mail
from django.db.models import Q

from .forms import InventarioForm

import datetime

# Create your views here.

def consulta(request):
	if request.user.is_authenticated:
		user_auth = request.user
		print (user_auth)
		search = request.GET.get('search','')
		filter_alumnos = request.GET.get('filter','')
		
		if search:
			query = Q(nombre__icontains=search) | Q(apellido__icontains=search)
			lista_alumnos = DatosPersonales.objects.filter(query)
			if user_auth.username == 'maestro' or user_auth.username == 'jperez':
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos, 'usuario':user_auth})
			else:
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
		
		elif filter_alumnos:
			try:
				a = filter_alumnos.split('_')
				a1 = a[0]
				a2 = a[1]
				lista_alumnos = DatosPersonales.objects.filter(escolaridad_alum__escolaridad=a1).filter(grado=a2).order_by('apellido')
				if user_auth.username == 'maestro' or user_auth.username == 'jperez':
					return render(request, 'alumnos.html', {'alumnos':lista_alumnos, 'usuario':user_auth})
				else:
					return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
			except:	
				lista_alumnos = DatosPersonales.objects.filter(escolaridad_alum__escolaridad=filter_alumnos).order_by('grado','apellido')
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
		else:
			lista_alumnos = DatosPersonales.objects.order_by('escolaridad_alum', 'grado','apellido')
			if user_auth.username == 'maestro' or user_auth.username == 'jperez':
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos, 'usuario':user_auth})
			else:
				
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
	
	else:
		return render(request, 'alumnos.html', {})

def consultaespecifica(request, id):
	if request.user.is_authenticated:
		instance = get_object_or_404(DatosPersonales, id=id)
		fecha_actual = datetime.datetime.now()
		mi_fecha = instance.nacimiento
		print (fecha_actual, mi_fecha)
		if ((fecha_actual.month <= mi_fecha.month) & (fecha_actual.day <= mi_fecha.day)):
			edad = fecha_actual.year - mi_fecha.year - 1
			print(edad)
		else:
			edad = fecha_actual.year - mi_fecha.year
			print(edad)

		return render(request, 'alumno_data.html', {'instance':instance, 'edad':edad})
	else:
		return render(request, 'alumno_data.html', {'autentificacion':'Favor de autentificarse'})

def inventario_update(request, id=None):
	instance = get_object_or_404(DatosPersonales, id=id)
	formulario = InventarioForm(request.POST or None, instance=instance)
	if formulario.is_valid():
		instance = formulario.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	return render(request, 'inventario_form.html', {'form':formulario,'instance': instance})

def correo(request):
	if request.user.is_authenticated:
		user_auth = request.user
		if user_auth.username == maestro:
			if form.is_valid():
			    subject = form.cleaned_data['subject']
			    message = form.cleaned_data['message']
			    sender = form.cleaned_data['sender']
			    cc_myself = form.cleaned_data['cc_myself']

			    recipients = ['info@example.com']
			    if cc_myself:
			        recipients.append(sender)

			    send_mail(subject, message, sender, recipients)
			    return HttpResponseRedirect('/thanks/')

def cumple(request):
	mes = datetime.datetime.now().month
	mes_letra = datetime.datetime.now()
	dia = datetime.datetime.now().day
	print(dia)
	instance = DatosPersonales.objects.filter(nacimiento__month=mes)
	context = {
		'mes':mes_letra, 'instance':instance, 'dia':dia
	}
	return render(request, 'cumple.html', context)
