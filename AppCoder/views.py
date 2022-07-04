from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NuevoProfesor
from .models import profesores


# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")

def anadir_profesor(request):
    
    if request.method == "POST":
        
        formulario = NuevoProfesor(request.POST)
    
        if formulario.is_valid():
            
            info_profesor = formulario.cleaned_data
            
            profesor = profesores(nombre = info_profesor["nombre"], apellido = info_profesor["apellido"], profesion = info_profesor["profesion"], salario = int(info_profesor["salario"]))
            profesor.save()
            
            return redirect("profesores")
        
        else:
            
            return render(request,"AppCoder/formulario_profesor.html",{"form":formulario})
        
    else:
        
        formularioVacio = NuevoProfesor()
        
        return render (request, "AppCoder/formulario_profesor.html", {"form":formularioVacio})