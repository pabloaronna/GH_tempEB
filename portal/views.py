from django.shortcuts import render
from django.http import HttpResponse
from appUsuarios.models import Usuario

def home(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'home/index.html', context)
# return HttpResponse('<h1> Pantalla HOME Portal</h1>')

def novedades(request):
   
    return render(request, 'home/novedades.html')