from django import forms
from enemigosapp.models import Enemigo
from django.core import validators

class FormEnemigo(forms.ModelForm):

    class Meta:
        model = Enemigo
        fields = '__all__'

        def clean_integers(self):
            inputNumeros = self.cleaned_data['asesinatos']
            if inputNumeros > 0:
                raise forms.ValidationError("No pueden ir números negativos")
            return inputNumeros