from django.urls import path
from Projeto_Joaninha.pedidos import views as v

app_name="pedidos"

urlpatterns=[
    path('',v.pedidos_list,name='pedidos_list'),
    path('<int:pk>/',v.pedidos_detail,name='pedidos_detail'),

]