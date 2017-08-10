from django.contrib import admin
from .models import Evento

class AdminEvento(admin.ModelAdmin):
	list_display = ['titulo', 'timestamp', 'date_update']
	search_field = ['titulo']
	list_filter = ['timestamp', 'date_update']
# Register your models here.
admin.site.register(Evento, AdminEvento)