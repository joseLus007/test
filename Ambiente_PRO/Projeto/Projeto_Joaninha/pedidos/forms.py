from django import forms
from .models import Pedidos

class PedidosForm(forms.ModelForm):
    nome_cliente=forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))

    email=forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Email"}))
    lista_pedidos=forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Pedido"}))

    endereco=forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "endereco"}))

    numero_contato=forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Contato"}))
    class Meta:
        model=Pedidos
        fields=["nome_cliente","email","lista_pedidos","endereco","numero_contato"]