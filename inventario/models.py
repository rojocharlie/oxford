from django.db import models


# Create your models here.

class Material(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class DetalleMaterial(models.Model):
    material = models.ForeignKey(Material)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.material.nombre


class Escuela(models.Model):
    nivel = models.CharField(max_length=20)

    def __str__(self):
        return self.nivel


class Maestro(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    escuela = models.ForeignKey(Escuela)

    def __str__(self):
        return self.nombre


class Vale(models.Model):
    no_folio = models.PositiveIntegerField(unique=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    maestro = models.ForeignKey(Maestro)
    material = models.ManyToManyField(DetalleMaterial)

    def __int__(self):
        return self.no_folio

    class Meta:
        ordering = ('no_folio',)
