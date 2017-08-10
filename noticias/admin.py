from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'fecha_publicacion', 'autor')
	list_filter = ('autor', 'fecha_publicacion')
	search_fields = ('titulo',)

# Register your models here.
admin.site.register(Noticia,NoticiaAdmin)