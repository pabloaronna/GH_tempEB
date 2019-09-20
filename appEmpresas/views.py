from django.shortcuts import render
from .models import Empresas
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from appUsuarios.models import Usuario
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import EmpresasModelForm

@login_required
def empresa_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(Empresas, slug=slug)
    template_name = 'appEmpresas/detail_view.html'
    context = {"empresa": obj}
    return render(request, template_name, context)   

@login_required
def empresa_lista_view(request):
    obj = Empresas.objects.filter(usuario=request.user)
    template_name = 'appEmpresas/lista_view.html'
    context = {"misEmpresas": obj}
    return render(request, template_name, context) 

@login_required
def empresa_delete_view(request, slug):
    template_name = 'appEmpresas/delete_view.html'
    obj = get_object_or_404(Empresas, slug=slug)
    context = {"object": obj}
    if request.method == "POST" and request.user.is_authenticated:
        obj.delete()
        messages.success(request, "Eliminada!")
        return HttpResponseRedirect("/empresa/lista/")

    
    return render(request, template_name, context)   


@login_required
def empresa_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    usuario = request.user
    form = EmpresasModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.instance.usuario = usuario
        obj = form.save(commit=False)
        obj.save()
        empresa = get_object_or_404(Empresas, slug=obj.slug)
        return redirect(empresa.get_info_url())

    template_name = 'appEmpresas/create_view.html'
    context = {'form': form, 'usuario': usuario,}
    return render(request, template_name, context)  
