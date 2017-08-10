from django.db import models

# Create your models here.
class Generacion(models.Model):
	nombre_generacion = models.CharField(max_length=15)

	def __str__(self):
		return self.nombre_generacion

class Mencion(models.Model):
	nombre_mencion_honorifica = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre_mencion_honorifica

class NivelEscolar(models.Model):
	nombre_nivel_escolar = models.CharField(max_length=15)

	def __str__(self):
		return self.nombre_nivel_escolar

class Listado(models.Model):
	nombre_alumno = models.CharField(max_length = 40)
	generacion = models.ForeignKey(Generacion)
	mencion_honorifica = models.ForeignKey(Mencion, null=True)
	nivel_escolar = models.ForeignKey(NivelEscolar, null=True)
	foto = models.ImageField(upload_to='img/fotos/egresados', null=True)

	def __str__ (self):
		return self.nombre_alumno