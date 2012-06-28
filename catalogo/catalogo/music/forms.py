# coding: utf-8

from django.forms import ModelForm

from .models import Artist

class ArtistModelForm(ModelForm):
	error_css_class = 'error'
	required_css_class = 'required'

	class Meta:
		model = Artist