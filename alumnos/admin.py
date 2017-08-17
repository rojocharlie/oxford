from django.contrib import admin
from .models import DatosPersonales, TipoSangre, Escolaridad, SexoModel, NivelIngles

class AdminDatosPersonales(admin.ModelAdmin):
	list_display = ('apellido','nombre', 'escolaridad_alum', 'grado', 'correo_escuela', 'foto')
	list_filter = ('escolaridad_alum', 'grado')
	search_fields = ('nombre', 'apellido','correo_escuela')
	

# Register your models here.
admin.site.register(DatosPersonales, AdminDatosPersonales)
admin.site.register(TipoSangre)
admin.site.register(Escolaridad)
admin.site.register(SexoModel)
admin.site.register(NivelIngles)