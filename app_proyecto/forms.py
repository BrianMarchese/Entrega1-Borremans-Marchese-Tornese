from django import forms


class Animal_forms(forms.Form):
    nombre= forms.CharField(max_length=50)
    tipo_animal= forms.CharField(max_length=50)

class Persona_forms(forms.Form):
    nombre= forms.CharField(max_length=50)
    edad= forms.IntegerField()

class Auto_forms(forms.Form):
    marca= forms.CharField(max_length=50)
    anio_fabricacion= forms.DateField()
    modelo= forms.CharField(max_length=50)

