from django.conf.urls import url
from noticias import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^noticia/(?P<id>\d+)/$', views.noticia_view, name='noticia_view'),
    url(r'^login/$', views.my_view , name='login'),
    url(r'^logout/$', views.logout_view , name='logout'),
]