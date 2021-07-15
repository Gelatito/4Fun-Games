from django import forms
from django.db import models
from django.db.models import fields
from core.models import Categorias, MundoAbierto



class MundoAbiertoForm(forms.ModelForm):

    class Meta:
        model=MundoAbierto
        fields ='__all__'

class CategoriasForm(forms.ModelForm):

    class Meta:
        model=Categorias
        fields ='__all__'





