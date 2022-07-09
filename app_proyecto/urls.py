from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path("auto/", auto_formulario, name="auto_form"),

]