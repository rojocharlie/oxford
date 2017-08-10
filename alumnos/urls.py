from django.conf.urls import url
from alumnos import views

urlpatterns = [
    url(r'^alumnos/$', views.consulta, name='alumnos'),
	url(r'^alumnos/(?P<id>\d+)/$', views.consultaespecifica, name='consulta'),
	url(r'^alumnos/inventario/update/(?P<id>\d+)/$', views.inventario_update, name='inv_update'),
	#url(r'^alumnos/inventario/nuevo/$', views.inventario_nuevo, name='inv_new'),
    ]
