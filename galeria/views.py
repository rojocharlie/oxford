from django.shortcuts import render, get_object_or_404
from .models import Evento

# Create your views here.
def evento(request):
	eventos = Evento.objects.all()
	return render(request, 'eventos.html', {'eventos':eventos})

def evento_galeria(request, id):
	instance = get_object_or_404(Evento, id=id)
	return render(request, 'evento_galeria.html', {'instance':instance})