from django.contrib import admin
from .models import Generacion, Listado, Mencion, NivelEscolar

class AdminListado(admin.ModelAdmin):
	list_display = ('nombre_alumno', 'generacion','foto',)
	list_filter = ('generacion',)
	search_fields = ('nombre_alumno',)

# Register your models here.
admin.site.register(Generacion)
admin.site.register(Mencion)
admin.site.register(Listado, AdminListado)
admin.site.register(NivelEscolar)