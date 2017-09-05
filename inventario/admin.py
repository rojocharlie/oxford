from django.contrib import admin
from .models import Escuela, Maestro, Material, Vale, DetalleMaterial

# Register your models here.

class AdminVale(admin.ModelAdmin):
	list_filter = ('maestro', 'fecha_publicacion')
	list_display = ('pk','no_folio', 'maestro', 'fecha_publicacion')

class AdminDetalle(admin.ModelAdmin):
	list_display = ('pk','material', 'cantidad')


admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Material)
admin.site.register(Vale, AdminVale)
admin.site.register(DetalleMaterial, AdminDetalle)