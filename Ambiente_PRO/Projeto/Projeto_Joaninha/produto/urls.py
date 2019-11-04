
from django.urls import path
from Projeto_Joaninha.produto import views as v

# este é o sepador de  paginas html 
app_name = 'produto'


urlpatterns = [
    path('',v.Produto_list, name='Produto_list'),
    path('<int:pk>/',v.Produto_detail, name='Produto_detail'),
    path('add/',v.ProdutoCreate.as_view(), name='Produto_add'),
    path('<int:pk>/edit',v.ProdutoUpdate.as_view(), name='Produto_edit'),
    
]   

