from django.urls import path
from AppCoder import views
from AppCoder.views import inicio, cursos, profesores, estudiantes, entregables



urlpatterns = [
    
    path('', views.inicio),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]