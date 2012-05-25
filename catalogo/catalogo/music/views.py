# Create your views here.

# coding: utf-8

from .models import Artist, Album, Song

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory

def listar_albuns(request):
	albuns = Album.objects.all()
	vars_template = {'albuns': albuns}
	return render(request, 'music/albuns.html', vars_template)