from django.db import models
from django.urls import reverse_lazy

class Pedidos(models.Model):
    nome_cliente=models.CharField('nome_cliente',max_length=100)
    email=models.CharField('E-mail',max_length=200,unique=True)
    lista_pedidos=models.CharField('pedidos',max_length=500)
    forma_de_pagamento=models.CharField('forma_de_pagamento', max_length=100)
    endereco=models.CharField('endereço',max_length=2000)
    numero_contato=models.CharField('contato',max_length=12)
    
    class Meta:
        ordering=("lista_pedidos",)

    def __str__(self):
        return self.lista_pedidos

    def get_absolute_url(self):
        return reverse_lazy("pedidos:pedidos_detail",kwargs={'pk':self.pk})

        
