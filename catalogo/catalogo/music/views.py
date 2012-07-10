# Create your views here.

# coding: utf-8

from .models import Artist, Album, Song
from .forms import ArtistModelForm

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory

def index(request):
	return render(request, 'music/index.html')

def list_artists(request):
	artists = Artist.objects.all().order_by('name')
	vars_template = {'artists': artists}
	return render(request, 'music/artists.html', vars_template)

def list_albuns(request, artist_id):
	albuns = Album.objects.filter(artist_id = artist_id).order_by('year')
	vars_template = {'albuns': albuns}
	return render(request, 'music/albuns.html', vars_template)

def list_songs(request, album_id):
	songs = Song.objects.filter(album_id = album_id).order_by('number')
	vars_template = {'songs': songs}
	return render(request, 'music/songs.html', vars_template)

def save_artist(request, artist_id):
	#import pdb; pdb.set_trace()
	if request.method == 'POST':
		a = Artist()
		formulario = ArtistModelForm(request.POST, prefix="saveArtist", instance=a)
		if formulario.is_valid():
			formulario.save()
			url = reverse('list_albuns', args=[a.id])
			return HttpResponse('<li><h2><a class="artist" href="#" id="artist{0}" name="{1}">{2}</a></h2><ul id="artist{0}_list"></ul></li>'.format(a.id, url, a.name))
		else:
			vars_template = {'formulario': formulario, 'artist_id': artist_id}
			return render(request, 'music/editar_artist.html', vars_template)
	else:
		formulario = ArtistModelForm(prefix="saveArtist", auto_id='%s')
		vars_template = {'formulario': formulario, 'artist_id': artist_id}
		return render(request, 'music/editar_artist.html', vars_template)