from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.detalle_evento, name='detalle_evento'),
    url(r'^evento/(?P<pk>[0-9]+)/editar/$', views.editar_evento, name='editar_evento'),
    url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
    url(r'^evento/(?P<pk>\d+)/remove/$', views.evento_remove, name='evento_remove'),
    url(r'^listar/evento/$', views.listar_eventos, name='listar_eventos'),
    url(r'persona/(?P<pk>[0-9]+)/$', views.detalle_persona, name='detalle_persona'),
    url(r'^persona/(?P<pk>[0-9]+)/editar/$', views.editar_persona, name='editar_persona'),
    #    url(r'^persona/(?P<pk>\d+)/eliminar/$', views.persona_remove, name='persona_remove'),

    url(r'^listar/persona/$', views.listar_personas, name='listar_personas'),
    url(r'^persona/nueva/$', views.persona_nueva, name='persona_nueva'),
    url(r'^persona/(?P<pk>\d+)/remove/$', views.persona_remove, name='persona_remove'),
    ]
