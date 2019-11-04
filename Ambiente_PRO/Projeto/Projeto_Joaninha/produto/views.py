from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import Produto
from .forms import ProdutoForm


@login_required
def Produto_list(request):
    template_name='produto_list.html'
    objects=Produto.objects.all()
    context={'object_list':objects}
    return render(request, template_name, context)


def Produto_detail(request,pk):
    template_name='produto_detail.html'
    obj=Produto.objects.get(pk=pk)
    context={'object':obj}
    return render(request, template_name, context)


def Produto_add(request):
    template_name='produto_form.html'
    return render(request,template_name)

class ProdutoCreate(CreateView):
    model=Produto
    template_name='produto_form.html'
    form_class=ProdutoForm

class ProdutoUpdate(UpdateView):
    model=Produto
    template_name='produto_form.html'
    form_class=ProdutoForm
