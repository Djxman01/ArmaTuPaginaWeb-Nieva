from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='personajes/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre 
