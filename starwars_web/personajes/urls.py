from django.urls import path
from .views import ListaPersonajesView, agregar_personaje
from .views import eliminar_personaje

urlpatterns = [
    path('', ListaPersonajesView.as_view(), name='personajes'),
    path('agregar/', agregar_personaje, name='agregar_personaje'),
    path('eliminar/<int:pk>/', eliminar_personaje, name='eliminar_personaje'),
]