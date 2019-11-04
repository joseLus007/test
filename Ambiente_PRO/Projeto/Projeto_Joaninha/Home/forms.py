from django import forms
from Projeto_Joaninha.pedidos.models import Pedidos


class PedidosForm(forms.ModelForm):
    class Meta:
        models=Pedidos
        fields="__all__"
