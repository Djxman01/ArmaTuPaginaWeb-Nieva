 Star Wars Page - Proyecto Final

Este es mi proyecto final para el curso de Python de CoderHouse, es una pagina desarrollada con Django y uniendo algo que me gusta mucho, "Star Wars". Se pueden ver, agregar, eliminar personajes y peliculas/series, registrarse, iniciar sesion, y mas.

Funcionalidades principales

#Registro de Usuario y Login con autenticacion.

#Vista de personajes que pueden llevar imagenes, descripciones y la opcion de eliminarlos.

#Vista de peliculas/series que pueden llevar imagenes, descripciones y la opcion de eliminarlas tambien.

#Formulario de carga de imagenes

#DetailView de cada personaje haciendo click en la imagen

#El inicio es mi "Sobre mi" 

#Utilizamos Bootstrap para faciltiar el diseño de la paginas

Tecnologías utilizadas:

#Django 5.2
#Python 3.11
#HTML5, CSS3 y Bootstrap 5
#Font Awesome para íconos
#Mensajes con django.contrib.messages
#Sistema de templates base con herencia
#Pillow para carga de imágenes


Como ejecutar el proyecto localmente: 

1) CLona mi repositorio : 
git clone https://github.com/Djxman01/ArmaTuPaginaWeb-Nieva.git
cd ArmaTuPaginaWeb-Nieva

2) Activa el entorno virtual: 
python -m venv .venv
.venv\Scripts\activate  

3) Instala las dependencias necesarias:
pip install -r requirements.txt

4) Hace las migraciones:
python manage.py migrate

5) Empeza a correr el servidor: 
python manage.py runserver


Estructura del proyecto:

starwars_web/
├── contenido/
├── personajes/
├── usuarios/
├── templates/
├── static/
├── media/
├── manage.py
└── README.md


Sobre mi: 
Desarollado por Maximo Nieva como el proyecto final del curso de Python en ,
trabajando con Django, formularios, autenticaciones y demas.
