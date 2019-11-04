from django import forms
from .models import Pedidos


class PedidosForm(forms.ModelForm):
    class Meta:
        models=Pedidos
        fields="__all__"
