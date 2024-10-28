from django import forms
from enemigosapp.models import Enemigo
from django.core import validators

class FormEnemigo(forms.ModelForm):

    class Meta:
        model = Enemigo
        fields = '__all__'