from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
"""
def profe_nuevo(request):
    profeN= Profesor(nombre="Pepe", apellido= "Python", email= "son@mail.com", profesion="biofisico")
    profeN.save()

    return HttpResponse(f"hemos guardado al profesor {profeN.nombre}")

def curso_nuevo (request):
    mi_curso_favorito = Curso(nombre= "Python", camada=47765)
    mi_curso_favorito.save()

    return HttpResponse(f"Bienvenidos al curso {mi_curso_favorito.nombre}")
"""

def inicio(request):
    a = 20
    return render(request, "AppCoder/inicio.html", {"a":a})

def ver_cursos(request):
    return HttpResponse("pagina de cursos")

def ver_profes(request):
    return HttpResponse("pagina de profesores")

def ver_entregables(request):
    return HttpResponse("pagina de entregables")

def crear_estudiantes(request):
    return render(request, "AppCoder/crear_estudiantes.html")

def crear_cursos(request):
    if request.method == 'POST':
        curso_nuevo = Curso(nombre=request.POST['nombre'], camada=request.POST['comision'])
        curso_nuevo.save()
        return render(request, "AppCoder/inicio.html")
   
    return render(request, "AppCoder/crear_cursos.html")

def crear_profes(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) 
        if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  profe_nuevo = Profesor(nombre=info["nombre"], apellido=info["apellido"],
                                      email=info["email"], profesion=info["profesion"])
                  profe_nuevo.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario()
 
        return render(request, "AppCoder/crear_profes.html", {"form": miFormulario})

def crear_estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  estudiante_nuevo = Estudiante(nombre=info["nombre"], apellido=info["apellido"],
                                      email=info["email"])
                  estudiante_nuevo.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EstudianteFormulario()
 
        return render(request, "AppCoder/crear_estudiantes.html", {"form": miFormulario})

def buscar_profes(request):
    return render(request, "AppCoder/buscar_profes.html")

def resultado_profes(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        profes_resultado = Profesor.objects.filter(apellido__iexact=apellido)
        return render(request, "AppCoder/resultado_profes.html", {"valor":apellido, "res":profes_resultado})
    else:
        return HttpResponse("No enviaste datos")
        
    return render(request, "AppCoder/resultado_profes.html")