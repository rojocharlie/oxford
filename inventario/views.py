from django.shortcuts import render, redirect
from .models import Vale, Escuela, Maestro, Material
from .forms import ValeForm, MaestroForm, MaterialForm
import datetime

# Create your views here.

def vale_add(request):
	form = ValeForm()
	last_folio = Vale.objects.order_by('-no_folio')[0]
	new_folio = 1 + last_folio.no_folio
	if request.method == 'POST':
		form = ValeForm(request.POST)
		if form.is_valid():
			obj = Vale(maestro = form.cleaned_data['maestro'], no_folio = new_folio)
			obj.save()

			material1 = form.cleaned_data['material_1']
			cantidad1 = form.cleaned_data['cantidad_1']
			p1 = Material(nombre=material1, cantidad=cantidad1)
			obj.material.add(p1)
			obj.save_m2m()


			return redirect('vale_add')
	return render(request, 'vale_add.html', {'formulario':form, 'folio':new_folio})

def vale_check(request):
	instance = Vale.objects.all()
	return render(request, 'vale_check.html', {'lista':instance})

def maestro_add(request):
	form = MaestroForm()
	if request.method == 'POST':
		form = MaestroForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('maestro_add')

	return render(request, 'maestro_add.html', {'formulario':form})

def maestro_edit(request):
	pass

def maestro_del(request):
	pass

def material_add(request):
	form = MaterialForm()
	if request.method == 'POST':
		form = MaterialForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('material_add')
	return render(request, 'material_add.html', {'formulario':form})

def material_edit(request):
	pass

def material_del(request):
	pass
