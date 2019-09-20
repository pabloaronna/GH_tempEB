from django.shortcuts import render
from django.http import HttpResponse
from appUsuarios.models import Usuario

def home(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'portal/index.html', context)
# return HttpResponse('<h1> Pantalla HOME Portal</h1>')

def novedades(request):
   
    return render(request, 'portal/novedades.html')