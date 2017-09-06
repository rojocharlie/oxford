from django.conf.urls import url
from noticias import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^noticia/(?P<id>\d+)/$', views.noticia_view, name='noticia_view'),
    url(r'^noticia/add', views.noticia_add, name='noticia_add'),
    url(r'^logout/$', views.logout_view , name='logout'),
]