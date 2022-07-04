from django import forms


class NuevoProfesor(forms.Form):

    nombre = forms.CharField(max_length=30,label="Nombre")
    apellido = forms.CharField(max_length=30,label="Apellido")
    profesion = forms.CharField(max_length=30,label="Profesion")
    salario = forms.IntegerField(min_value=0,label="Salario")