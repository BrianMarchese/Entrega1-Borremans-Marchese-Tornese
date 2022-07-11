from enum import auto
from django.http import HttpResponse
from django.shortcuts import render
from app_proyecto.forms import *
from app_proyecto.models import *
# Create your views here.

def inicio(request):
    return render (request, "app_proyecto/inicio.html")

def animal_formulario(request):
    if (request.method=="POST"):
        form= Animal_forms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            tipo_animal= info["tipo_animal"]
            animal= Animal(nombre=nombre, tipo_animal=tipo_animal)
            animal.save()
            return render (request, "app_proyecto/inicio.html")
    else:
        formulario= Animal_forms()
    return render(request, "app_proyecto/animal_form.html", {"formulario":formulario})

def persona_formulario(request):
    if (request.method=="POST"):
        form= Persona_forms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            edad= info["edad"]
            persona= Persona(nombre=nombre, edad=edad)
            persona.save()
            return render (request, "app_proyecto/inicio.html")
    else:
        formulario= Persona_forms()
    return render(request, "app_proyecto/persona_form.html", {"formulario":formulario})

def auto_formulario(request):
    if (request.method=="POST"):
        form= Auto_forms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca= info["marca"]
            anio_fabricacion= info["anio_fabricacion"]
            modelo= info['modelo']
            auto= Auto(marca=marca, anio_fabricacion=anio_fabricacion, modelo=modelo)
            auto.save()
            return render (request, "app_proyecto/inicio.html")
    else:
        formulario= Auto_forms()
    return render(request, "app_proyecto/auto_form.html", {"formulario":formulario})

def buscar_persona(request):

    return render(request, "app_proyecto/buscar_persona.html")

def buscar_bd(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        persona= Persona.objects.filter(nombre=nombre)
        return render(request, "app_proyecto/busqueda_persona.html", {"persona":persona})

    else:
        return render(request, "app_proyecto/buscar_persona.html", {"error": "No se ingreso ninguna persona"})