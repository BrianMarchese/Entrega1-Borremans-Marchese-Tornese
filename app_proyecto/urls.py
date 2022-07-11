from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path('auto/', auto_formulario, name="auto_form"),
    path('persona/', persona_formulario, name="persona_form"),
    path('animal/', animal_formulario, name="animal_form"),
    path('buscar_persona/', buscar_persona, name="buscar_persona"),
    path('buscar_bd/', buscar_bd, name="buscar_bd"),
    path('buscar_auto/', buscar_auto, name="buscar_auto"),
    path('buscar_bd_auto/', buscar_bd_auto, name="buscar_bd_auto"),
    path('buscar_animal/', buscar_animal, name="buscar_animal"),
    path('buscar_bd_animal/', buscar_bd_animal, name="buscar_bd_animal"),

]