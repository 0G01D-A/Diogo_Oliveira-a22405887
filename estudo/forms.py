from django import forms
from .models import Atleta,Desporto


class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ['nome','idade','fotografia','desportos']


