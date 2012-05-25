# coding:utf-8

from django.conf.urls import patterns, include, url

from .views import listar_albuns

urlpatterns = patterns('',

    url(r'^albuns/', listar_albuns,name='listar_albuns'),

)
