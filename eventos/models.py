from django.db import models
from django.contrib import admin


class Evento(models.Model):
    nombre =   models.CharField(max_length=50)
    fecha_evento = models.DateField()
    descripcion= models.CharField(max_length=300)
    capacidad = models.IntegerField()
        
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre  =   models.CharField(max_length=50)
    edad =      models.IntegerField()
    telefono = models.IntegerField()
    eventos   = models.ManyToManyField(Evento, null=True,blank=True)

    def __str__(self):
        return self.nombre