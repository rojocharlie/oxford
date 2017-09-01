from django.contrib import admin
from .models import Escuela, Maestro, Material, Vale

# Register your models here.

admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Material)
admin.site.register(Vale)