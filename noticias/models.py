from django.db import models

# Create your models here.
class Noticia(models.Model):
	titulo = models.CharField(max_length=50)
	imagen_encabezado = models.ImageField(upload_to='noticias')
	texto_principal = models.TextField()
	video = models.FileField(upload_to='videos', blank=True, null=True)
	imagen_secundaria = models.ImageField(upload_to='noticias', null=True, blank=True)
	texto_secundario = models.TextField(null=True, blank=True)
	imagen_terciaria = models.ImageField(upload_to='noticias', null=True, blank=True)
	texto_terciaria = models.TextField(null=True, blank=True)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateField(auto_now=True)
	link_galeria = models.URLField(max_length=250, null=True, blank=True)
	autor = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.titulo