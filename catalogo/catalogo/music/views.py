# Create your views here.

# coding: utf-8

from .models import Artist, Album, Song

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory

def index(request):
	return render(request, 'music/index.html')

def listar_artists(request):
	artists = Artist.objects.all()
	vars_template = {'artists': artists}
	return render(request, 'music/artists.html', vars_template)

def listar_albuns(request, artist_id):
	albuns = Album.objects.filter(artist_id = artist_id).order_by('year')
	vars_template = {'albuns': albuns}
	return render(request, 'music/albuns.html', vars_template)

def listar_songs(request, album_id):
	songs = Song.objects.filter(album_id = album_id).order_by('number')
	vars_template = {'songs': songs}
	return render(request, 'music/songs.html', vars_template)	