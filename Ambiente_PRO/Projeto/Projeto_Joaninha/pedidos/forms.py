from django.forms import ModelForm
from .models import Pedidos


class PedidosForm(ModelForm):
    class Meta:
        models=Pedidos
        fields="__all__"

