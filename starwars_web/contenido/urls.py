from django.urls import path
from .views import ListaPeliculasView, agregar_peliculas
from .views import eliminar_peliculas
from . import views


urlpatterns = [
    path('', ListaPeliculasView.as_view(), name='peliculas'),
    path('agregar/', agregar_peliculas, name='agregar_peliculas'),
    path('eliminar/<int:pk>/', eliminar_peliculas, name='eliminar_peliculas'),
]
