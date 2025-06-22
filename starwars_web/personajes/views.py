from django.shortcuts import render, redirect
from .forms import PersonajeForm
from .models import Personaje
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages

class ListaPersonajesView(ListView):
    model = Personaje
    template_name = 'personajes/personajes.html'
    context_object_name = 'personajes'

def agregar_personaje(request):
    if request.method == 'POST':
        form = PersonajeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personajes')  # redirige a la lista de personajes
    else:
        form = PersonajeForm()
    
    return render(request, 'personajes/agregar_personaje.html', {'form': form})

def eliminar_personaje(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    personaje.delete()
    messages.success(request, f'Personaje "{personaje.nombre}" eliminado correctamente.')
    return redirect('personajes')