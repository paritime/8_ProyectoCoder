from django.db import models

# Create your models here.


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    edad = models.IntegerField()


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=40)


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
