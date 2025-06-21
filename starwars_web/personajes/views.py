from django.shortcuts import render

from .models import Personaje

def vistaPersonaje(request):
    personajes = Personaje.objects.all()
    return render(request, 'personajes/personajes.html', {'Personajes': personajes})

