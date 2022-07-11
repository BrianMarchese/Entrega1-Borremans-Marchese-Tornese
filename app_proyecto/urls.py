from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path('auto/', auto_formulario, name="auto_form"),
    path('persona/', persona_formulario, name="persona_form"),
    path('animal/', animal_formulario, name="animal_form"),
    path('buscar_persona/', buscar_persona, name="buscar_persona"),
    path('buscar_bd/', buscar_bd, name="buscar_bd"),


]