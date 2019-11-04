import os
import django
from Projeto_Joaninha.pedidos.models import Pedidos

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Projeto_Joaninha.settings")
django.setup()

def main ():
    t=Pedidos()
    t.nome_cliente='jose luis'
    t.email='jose@hotmail.com'
    t.lista_pedidos='Arroz,fejao,bife'
    t.forma_de_pagamento='Cartão'
    t.endereco='rua nao sei'
    t.numero_contato='9121222'

main()
