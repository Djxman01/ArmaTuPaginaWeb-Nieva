# contenido/views.py
from django.shortcuts import render

def vistaPeliculas(request):
    return render(request, 'contenido/peliculas.html')
