from django.conf.urls import url
from egresados import views

urlpatterns = [
	url(r'^egresados/$', views.generaciones , name='egresados'),
	url(r'^egresados/generacion/(?P<generacion>\w+)/$', views.visita , name='generacion'),
]