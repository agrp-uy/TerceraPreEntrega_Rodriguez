from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import *

# Create your views here.
def inicio(request):
    return render(request, "AppWeb/inicio.html")

def bebida(request):
    return render(request, "AppWeb/bebidas.html")

def comida(request):
    return render(request, "AppWeb/comidas.html")

def postre(request):
    return render(request, "AppWeb/postres.html")
