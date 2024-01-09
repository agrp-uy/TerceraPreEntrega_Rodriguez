from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import *

# Create your views here.
def bebida(request):
    bebida1 = Bebida.objects.get(nombre="Coca Cola")