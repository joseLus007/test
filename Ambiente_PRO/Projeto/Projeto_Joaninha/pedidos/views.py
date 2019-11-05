from django.shortcuts import render
from .models import Pedidos
from django.views.generic import CreateView
from .forms import PedidosForm
# ::::::::::::::::::::::::::::


def pedidos_list(request):
    template_name='pedidos_list.html'
    objects=Pedidos.objects.all()
    context={'object_list':objects}
    return render (request,template_name,context)

def pedidos_detail(request,pk):
    template_name="pedidos_detail.html"
    obj=Pedidos.objects.get(pk=pk)
    context={'object':obj}
    return render(request,template_name,context)

def pedidos_add(request):
    template_name='CardapioEntrega.html'
    return render (request,template_name)

class PedidosCreate(CreateView):
    model=Pedidos
    template_name='CardapioEntrega.html'
    form_class=PedidosForm


def pedidos_create(request):
    form_class=PedidosForm()
    if (request.method == 'POST'):
        form_class=PedidosForm(request.POST)
        if (form_class.is_valid()):
            dados_nome=form_class.cleaned_data['nome']
            dados_email=form_class.cleaned_data['email']
            dados_lista_pedidos=form_class.cleaned_data['lista_pedidos']
            dados_endereco=form_class.cleaned_data['endereco']
            dados_numero_contato=form_class.cleaned_data['numero_contato']
            new_post=POST(nome=dados_nome,
                          email=dados_email,
                          lista_pedidos=dados_lista_pedidos,
                          endereco=dados_endereco,
                          numero_contato=dados_numero_contato)
            new_post.save()
            
