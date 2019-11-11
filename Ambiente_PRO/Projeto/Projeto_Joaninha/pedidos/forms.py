from django import forms
from .models import Pedidos

class PedidosForm(forms.ModelForm):
    class Meta:
        model=Pedidos
        fields="__all__"