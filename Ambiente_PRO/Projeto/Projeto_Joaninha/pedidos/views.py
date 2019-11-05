from django.shortcuts import render
from .models import Pedidos
from django.views.generic import CreateView
from .forms import PedidosForm


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