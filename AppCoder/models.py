from django.db import models

# Create your models here.
class Cursos(models.Model):
    
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    salario = models.IntegerField()
    
class entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()