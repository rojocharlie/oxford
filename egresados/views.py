from django.shortcuts import render, get_object_or_404
from .models import Listado, Generacion

# Create your views here.
def visita(request, generacion):
	instance = generacion
	alumnos = Listado.objects.filter(generacion__nombre_generacion=instance).order_by('nombre_alumno')
	return render(request,'galeria_egresados.html', {'alumnos': alumnos, 'generacion':instance})

def generaciones(request):
	instance = Generacion.objects.all()
	return render(request, 'generaciones.html', {'generaciones':instance})