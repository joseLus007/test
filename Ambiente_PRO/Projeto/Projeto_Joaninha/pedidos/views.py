from django.shortcuts import render
from django.views.generic import CreateView
from .models import Pedidos
from .forms import PedidosForm
from django.urls import reverse_lazy


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



def pedido_create_view(request):
    form = PedidosForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PedidosForm()
    context = {
        'form': form
    }
    return render(request, "CardapioEntrega.html", context)