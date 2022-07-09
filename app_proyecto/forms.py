from django import forms


class animal_forms(forms.Form):
    nombre= forms.CharField(max_length=50)
    tipo_animal= forms.CharField(max_length=50)

class persona_forms(forms.Form):
    nombre= forms.CharField(max_length=50)
    edad= forms.IntegerField()

class auto_forms(forms.Form):
    marca= forms.CharField(max_length=50)
    anio_fabricacion= forms.IntegerField()
    modelo= forms.CharField(max_length=50)

