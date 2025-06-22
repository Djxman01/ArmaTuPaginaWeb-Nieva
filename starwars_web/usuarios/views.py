from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # inicia sesión automáticamente
            messages.success(request, '¡Usuario registrado con éxito!')
            return redirect('inicio')  # redirige al home después del registro
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


def login_view(request):
    error = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            usuario = authenticate(request, username=nombre, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                error = "Usuario o contraseña incorrectos"
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form, 'error': error})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')