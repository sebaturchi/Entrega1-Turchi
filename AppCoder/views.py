from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from .models import *

# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    
    cursos = Cursos.objects.all()
    
    return render(request,"AppCoder/cursos.html", {"cursos":cursos})

def profesores(request):
    
    profesores = Profesores.objects.all()
    
    return render(request,"AppCoder/profesores.html",{"profesores":profesores})

def estudiantes(request):
    
    estudiantes = Estudiantes.objects.all()
    
    return render(request,"AppCoder/estudiantes.html",{"estudiantes":estudiantes})

def entregables(request):
    return render(request,"AppCoder/entregables.html")

def anadir_profesor(request):
    
    if request.method == "POST":
        
        formulario = NuevoProfesor(request.POST)
    
        if formulario.is_valid():
            
            info_profesor = formulario.cleaned_data
            
            profesor = Profesores(nombre=info_profesor["nombre"], apellido=info_profesor["apellido"], profesion=info_profesor["profesion"], salario=int(info_profesor["salario"]))
            profesor.save()
            
            return redirect("profesores")
        
        else:
            
            return render(request,"AppCoder/formulario_profesor.html",{"form":formulario})
        
    else:
        
        formularioVacio = NuevoProfesor()
        
        return render (request, "AppCoder/formulario_profesor.html", {"form":formularioVacio})
    
def anadir_curso(request):
    
    if request.method == "POST":
        
        formulario = NuevoCurso(request.POST)
    
        if formulario.is_valid():
            
            info_curso = formulario.cleaned_data
            
            curso = Cursos(nombre=info_curso["nombre"], comision=info_curso["comision"])
            curso.save()
            
            return redirect("cursos")
        
        else:
            
            return render(request,"AppCoder/formulario_curso.html",{"form":formulario})
        
    else:
        
        formularioVacio = NuevoCurso()
        
        return render (request, "AppCoder/formulario_curso.html", {"form":formularioVacio})
    
def anadir_estudiante(request):
    
    if request.method == "POST":
        
        formulario = NuevoAlumno(request.POST)
    
        if formulario.is_valid():
            
            info_alumno = formulario.cleaned_data
            
            alumno = Estudiantes(nombre=info_alumno["nombre"], apellido=info_alumno["apellido"], email=info_alumno["email"])
            alumno.save()
            
            return redirect("estudiantes")
        
        else:
            
            return render(request,"AppCoder/formulario_estudiante.html",{"form":formulario})
        
    else:
        
        formularioVacio = NuevoAlumno()
        
        return render (request, "AppCoder/formulario_estudiante.html", {"form":formularioVacio})
    
def buscar_comision(request):
      
    if request.method == "POST":
          
        comision = request.POST["comision"]
          
        comisiones = Cursos.objects.filter(comision__icontains=comision)
        
        return render(request,"AppCoder/busqueda_comision.html", {"comisiones":comisiones})
    
    else:
    
        comisiones = [] #Cursos.objects.all()
    
        return render(request,"AppCoder/busqueda_comision.html", {"comisiones":comisiones})
    
