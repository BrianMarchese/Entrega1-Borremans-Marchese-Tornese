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
        form= animal_forms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            tipo_animal= info["tipo_animal"]
            animal= Animal(nombre=nombre, tipo_animal=tipo_animal)
            animal.save()
            return render (request, "app_proyecto/inicio.html")
    else:
        form= animal_forms()
    return render(request, "app_proyecto/animal_formulario.html", {"formulario":form})

def persona_formulario(request):
    if (request.method=="POST"):
        form= persona_forms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            edad= info["edad"]
            persona= Persona(nombre=nombre, edad=edad)
            persona.save()
            return render (request, "app_proyecto/inicio.html")
    else:
        form= persona_forms()
    return render(request, "app_proyecto/persona_formulario.html", {"formulario":form})

def auto_formulario(request):
    if (request.method=="POST"):
        form= auto_forms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca= info["marca"]
            anio= info["anio"]
            modelo= info['modelo']
            auto= Auto(marca=marca, anio=anio, modelo=modelo)
            auto.save()
            return render (request, "app_proyecto/inicio.html")
    else:
        form= animal_forms()
    return render(request, "app_proyecto/auto_formulario.html", {"formulario":form})
