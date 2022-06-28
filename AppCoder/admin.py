from django.contrib import admin
from AppCoder.models import cursos, entregables, estudiantes, profesores

# Register your models here.

admin.site.registrer(cursos)

admin.site.registrer(entregables)

admin.site.registrer(estudiantes)

admin.site.registrer(profesores)