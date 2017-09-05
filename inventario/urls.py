from django.conf.urls import url
from inventario import views

urlpatterns = [
	url(r'^inventario/vale/add/$', views.vale_add , name='vale_add'),
	url(r'^inventario/vale/check/$', views.vale_check , name='vale_check'),
	url(r'^inventario/maestro/add/$', views.maestro_add , name='maestro_add'),
	url(r'^inventario/material/add/$', views.material_add , name='material_add'),
]