from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from alumnos.models import DatosPersonales
from django.db.models import Q
from .forms import InventarioForm
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
			return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
		
		elif filter_alumnos:
			try:
				a = filter_alumnos.split('_')
				a1 = a[0]
				a2 = a[1]
				lista_alumnos = DatosPersonales.objects.filter(escolaridad_alum__escolaridad=a1).filter(grado=a2).order_by('apellido')
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
			except:	
				lista_alumnos = DatosPersonales.objects.filter(escolaridad_alum__escolaridad=filter_alumnos).order_by('grado','apellido')
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
		else:
			if user_auth.username == 'maestro':
				lista_alumnos = DatosPersonales.objects.order_by('escolaridad_alum', 'grado','apellido')
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos, 'usuario':user_auth})
			else:
				lista_alumnos = DatosPersonales.objects.order_by('escolaridad_alum', 'grado','apellido')
				return render(request, 'alumnos.html', {'alumnos':lista_alumnos})
	
	else:
		return render(request, 'alumnos.html', {})

def consultaespecifica(request, id):
	if request.user.is_authenticated:
		instance = get_object_or_404(DatosPersonales, id=id)
		return render(request, 'alumno_data.html', {'instance':instance})
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