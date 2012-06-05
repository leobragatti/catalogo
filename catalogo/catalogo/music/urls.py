# coding:utf-8

from django.conf.urls import patterns, include, url

from .views import listar_artists, listar_albuns, listar_songs, index

urlpatterns = patterns('',

	url(r'^artists/', listar_artists, name='listar_artists'),
    url(r'^albuns/(\d+)', listar_albuns, name='listar_albuns'),
    url(r'^songs/(\d+)', listar_songs, name='listar_songs'),
	url(r'', index, name='pagina_inicial'),

)