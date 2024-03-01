from django import forms
from django.forms.widgets import DateInput


class Entregable_form (forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaEntrega = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    entregado = forms.BooleanField()
