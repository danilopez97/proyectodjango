from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.detalle_evento, name='detalle_evento'),
   
    url(r'^evento/(?P<pk>[0-9]+)/editar/$', views.editar_evento, name='editar_evento'),
    
    
    
    url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
    url(r'^evento/(?P<pk>\d+)/remove/$', views.evento_remove, name='evento_remove'),
    
    url(r'^listar/evento/$', views.listar_eventos, name='listar_eventos'),
    ]