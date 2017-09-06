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

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = DatosPersonales
		fields = (
		'nombre',
		'apellido',
		'correo',
		'correo_escuela',
		'sexo_alumno',
		'nacimiento',
		'escolaridad_alum',
		'grado',
		'direccion',
		'colonia',
		'cp',
		'telefono',
		'celular',
		'foto',
		'nivel_ingles',
		'notas',
		'catecismo',
		'serviciomedico',
		'sangre',
		'alergias',
		'enfermedadcronica',

		'nombrepadre',
		'correopadre',
		'ocupacionpadre',
		'trabajopadre',
		'telpadre',
		'celpadre',

		'nombremadre',
		'correomadre',
		'ocupacionmadre',
		'trabajomadre',
		'telmadre',
		'celmadre',

		'nombreautorizada',
		'parentesco',
		'ocupacionaut',
		'trabajoaut',
		'telaut',
		'celaut',
		)