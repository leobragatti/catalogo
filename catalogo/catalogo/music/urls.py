# coding:utf-8

from django.conf.urls import patterns, include, url

from .views import listar_albuns, listar_songs, index

urlpatterns = patterns('',

    url(r'^albuns/', listar_albuns, name='listar_albuns'),
    url(r'^songs/(\d+)', listar_songs, name='listar_songs'),
	url(r'', index, name='pagina_inicial'),

)