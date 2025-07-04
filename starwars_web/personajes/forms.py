from django import forms
from .models import Personaje

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['nombre', 'descripcion', 'imagen']
