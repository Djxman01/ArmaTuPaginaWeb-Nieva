from django.shortcuts import render, redirect
from .forms import PeliculasForm
from .models import Peliculas
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages

class ListaPeliculasView(ListView):
    model = Peliculas
    template_name = 'contenido/peliculas.html'
    context_object_name = 'contenido'

def agregar_peliculas(request):
    if request.method == 'POST':
        form = PeliculasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('peliculas')  # redirige a la lista de personajes
    else:
        form = PeliculasForm()
    
    return render(request, 'contenido/agregar_peliculas.html', {'form': form})


def eliminar_peliculas(request, pk):
    pelicula = get_object_or_404(Peliculas, pk=pk)
    pelicula.delete()
    messages.success(request, f'Pelicula "{pelicula.nombre}" eliminado correctamente.')
    return redirect('peliculas')