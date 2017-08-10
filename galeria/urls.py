from django.conf.urls import url
from galeria import views

urlpatterns = [
    url(r'^eventos/$', views.evento, name='eventos'),
    url(r'^eventos/(?P<id>\d+)/$', views.evento_galeria, name='evento'),
    ]
