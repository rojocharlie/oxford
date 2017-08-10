from django.db import models

# Create your models here.
class Evento(models.Model):
	titulo = models.CharField(max_length=30)
	date_update = models.DateTimeField(auto_now=True, auto_now_add=False,  editable = False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, editable = False)
	foto1 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto2 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto3 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto4 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto5 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto6 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto7 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto8 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto9 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto10 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto11 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto12 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto13 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto14 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto15 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto16 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto17 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto18 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto19 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto20 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto21 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto22 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto23 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto24 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto25 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto26 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto27 = models.ImageField(upload_to='img/evento/', blank=True, null=True)
	foto28 = models.ImageField(upload_to='img/evento/', blank=True, null=True)

	def __str__(self):
		return self.titulo