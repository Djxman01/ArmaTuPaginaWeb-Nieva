from django.shortcuts import render

def login_view(request):
    return render(request, 'usuarios/login.html')
    
def vistaRegistro(request):
    return render(request, 'usuarios/registro.html')