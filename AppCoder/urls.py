from django.urls import path
from .views import *



urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name = 'profesores'),
    path('estudiantes/', estudiantes, name = 'estudiantes'),
    path('entregables/', entregables, name = 'entregables'),
    path('anadir_profesor/', anadir_profesor, name="anadir_profesor"),
    path('anadir_curso/', anadir_curso, name="anadir_curso"),
    path('anadir_estudiante/', anadir_estudiante, name="anadir_estudiante"),
    path('buscar_comision/', buscar_comision, name="buscar_comision"),
]