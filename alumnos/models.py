from django.db import models
from django.core.urlresolvers import reverse

class NivelIngles(models.Model):
	nivel = models.CharField(max_length=1)

	def __str__(self):
		return self.nivel

class SexoModel(models.Model):
	sexo = models.CharField(max_length=1)

	def __str__(self):
		return self.sexo

class Escolaridad(models.Model):
	escolaridad = models.CharField(max_length=10) #Escolaridad

	def __str__(self):
		return self.escolaridad

class TipoSangre(models.Model):
	sangre = models.CharField(max_length=3) #Tipo de Sangre

	def __str__(self):
		return self.sangre

# Create your models here.
class DatosPersonales(models.Model):
	nombre = models.CharField(max_length=40) #Nombre del alumno
	apellido = models.CharField(max_length=30, default='Apellido') #Apellido del alumno
	correo = models.EmailField(max_length=50, blank=True, null=True) #Correo del alumno
	sexo_alumno = models.ForeignKey(SexoModel, blank=True, null=True)
	nacimiento = models.DateField() #Fecha de nacimiento del alumno
	escolaridad_alum = models.ForeignKey(Escolaridad) #Escolaridad
	grado = models.IntegerField() #Grado
	direccion = models.CharField(max_length=50) #Direccion
	colonia = models.CharField(max_length=20) #Colonia
	cp = models.CharField(max_length=10) #Codigo postal
	telefono = models.CharField(max_length=10) #Telefono
	celular = models.CharField(max_length=10) #Celular
	foto = models.ImageField(upload_to= 'img/fotos', blank=True, null=True)
	nivel_ingles = models.ForeignKey(NivelIngles, blank=True, null=True)
	notas = models.TextField(max_length=100, blank=True, null=True) #Notas
	catecismo = models.CharField(max_length=10, blank=True, null=True) #Catecismo
	serviciomedico = models.CharField(max_length=25, blank=True, null=True) #Servicio medico
	sangre = models.ForeignKey(TipoSangre, blank=True, null=True) #Tipo de sangre
	alergias = models.CharField(max_length=60, blank=True, null=True) #Alergias
	enfermedadcronica = models.CharField(max_length=60, blank=True, null=True) #Enfermedades cronicas

	nombrepadre = models.CharField(max_length=50, blank=True, null=True) #Nombre del padre
	correopadre = models.EmailField(max_length=50, blank=True, null=True) #Correo del padre
	ocupacionpadre = models.CharField(max_length=20, blank=True, null=True) #Ocupacion
	trabajopadre = models.CharField(max_length=50, blank=True, null=True) #Lugar donde labora
	telpadre = models.CharField(max_length=10, blank=True, null=True) #Telefono
	celpadre = models.CharField(max_length=10, blank=True, null=True) #Celular

	nombremadre = models.CharField(max_length=50, blank=True, null=True) #Nombre del padre
	correomadre = models.EmailField(max_length=50, blank=True, null=True) #Correo del madre
	ocupacionmadre = models.CharField(max_length=20, blank=True, null=True) #Ocupacion
	trabajomadre = models.CharField(max_length=20, blank=True, null=True) #Lugar donde labora
	telmadre = models.CharField(max_length=10, blank=True, null=True) #Telefono
	celmadre = models.CharField(max_length=10, blank=True, null=True) #Celular

	nombreautorizada = models.CharField(max_length=50, blank=True, null=True) #Nombre del padre
	parentesco = models.CharField(max_length=15, blank=True, null=True) #Parentesco con el alumno
	ocupacionaut = models.CharField(max_length=30, blank=True, null=True) #Ocupacion
	trabajoaut = models.CharField(max_length=50, blank=True, null=True) #Lugar donde labora
	telaut = models.CharField(max_length=10, blank=True, null=True) #Telefono
	celaut = models.CharField(max_length=10, blank=True, null=True) #Celular
	
	candado = models.IntegerField(default=0)
	papel_china = models.IntegerField(default=0)
	papel_crepe = models.IntegerField(default=0)
	rotafolio_blanco = models.IntegerField(default=0)
	rotafolio_cuadrado = models.IntegerField(default=0)
	papelbond_colores = models.IntegerField(default=0)
	paquete_500hojas_blanca = models.IntegerField(default=0)
	papeles_trasa_metro = models.IntegerField(default=0)
	caja_conos = models.IntegerField(default=0)
	paquete_papel_sanitario = models.IntegerField(default=0)
	paquete_toallas_papel = models.IntegerField(default=0)
	caja_pañuelos = models.IntegerField(default=0)

	def __str__(self):
		return '%s %s' % (self.apellido, self.nombre)

	def get_absolute_url(self):
		return reverse('consulta', kwargs={'id':self.id})