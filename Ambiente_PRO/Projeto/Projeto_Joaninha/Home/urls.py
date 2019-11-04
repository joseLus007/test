from django.urls import path
from . import views as v
from Projeto_Joaninha.pedidos import views as vi

app_name='home'
urlpatterns = [
    path('',v.Home, name='Home'),
    path('somos/',v.QuemSomos, name='QuemSomos'),
    path('local/',v.Localizacao, name='Localizacao'),
    path('CardapioEntrega/', vi.PedidosCreate.as_view(), name='CardapioEntrega'),
    path('Agradecimentos/', v.Agradecimentos, name='Agradecimentos')
]
