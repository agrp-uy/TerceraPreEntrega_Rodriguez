from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import *

# Create your views here.
def inicio(request):
    return render(request, "AppWeb/inicio.html")

def bebida(request):
    return render(request, "AppWeb/bebida.html")

def comida(request):
    return render(request, "AppWeb/comida.html")

def postre(request):
    return render(request, "AppWeb/postre.html")

def carta(request):
    return render(request, "AppWeb/carta.html")

def pedido(request):
    return render(request, "AppWeb/pedido.html")
