"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppWeb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #URLs de la app
    path('', inicio, name='Inicio'),
    path('inicio/', inicio, name='Inicio'),
    path('carta/', carta, name='Carta'),
    path('pedido/', pedido, name='Pedido'),

    #URLs de los modelos creados
    path('comida/', comida, name='Comidas'),
    path('bebida/', bebida, name='Bebidas'),
    path('guarnicion/', guarnicion, name='Guarniciones'),
    path('postre/', postre, name='Postres'),

    #URLs para agregar elementos
    path('agregarComida/', agregarComida, name='Agregar Comida'),
    path('agregarBebida/', agregarBebida, name='Agregar Bebida'),
    path('agregarGuarnicion/', agregarGuarnicion, name='Agregar Guarnicion'),
    path('agregarPostre/', agregarPostre, name='Agregar Postre'),

    #URLs para buscar elementos
    path('buscarComida/', buscarComida, name='Buscar Comida'),
    path('resultadosComida/', resultadosComida, name='Resultados Comida'),
    path('buscarBebida/', buscarBebida, name='Buscar Bebida'),
    path('resultadosBebida/', resultadosBebida, name='Resultados Bebida'),
    path('buscarGuarnicion/', buscarGuarnicion, name='Buscar Guarnicion'),
    path('resultadosGuarnicion/', resultadosGuarnicion, name='Resultados Guarnicion'),
    path('buscarPostre/', buscarPostre, name='Buscar Postre'),
    path('resultadosPostre/', resultadosPostre, name='Resultados Postre'),

]
