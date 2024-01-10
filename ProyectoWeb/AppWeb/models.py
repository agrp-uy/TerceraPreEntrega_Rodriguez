from django.db import models

# Create your models here.

class Comida(models.Model):
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

class Bebida(models.Model):
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

class Postre(models.Model):
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()