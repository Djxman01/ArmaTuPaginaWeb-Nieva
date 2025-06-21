from django.urls import path
from . import views

urlpatterns = [
    path('personajes/', views.vistaPersonaje, name='personajes'),
]
