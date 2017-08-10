from django import forms
from .models import DatosPersonales

class InventarioForm(forms.ModelForm):
	class Meta:
		model = DatosPersonales
		fields = ('candado',
		'papel_china',
		'papel_crepe',
		'rotafolio_blanco',
		'rotafolio_cuadrado',
		'papelbond_colores',
		'paquete_500hojas_blanca',
		'papeles_trasa_metro',
		'caja_conos',
		'paquete_papel_sanitario',
		'paquete_toallas_papel', 
		'caja_pañuelos', )