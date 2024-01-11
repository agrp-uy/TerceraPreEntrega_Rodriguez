from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import *
from AppWeb.forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppWeb/inicio.html")

def comida(request):
    mis_comidas = Comida.objects.all()
    info_comidas = {'comidas': mis_comidas}
    return render(request, "AppWeb/comida.html", info_comidas)

def bebida(request):
    mis_bebidas = Bebida.objects.all()
    info_bebidas = {'bebidas': mis_bebidas}
    return render(request, "AppWeb/bebida.html", info_bebidas)

def guarnicion(request):
    mis_guarniciones = Guarnicion.objects.all()
    info_guarniciones = {'guarniciones': mis_guarniciones}
    return render(request, "AppWeb/guarnicion.html", info_guarniciones)

def postre(request):
    mis_postres = Postre.objects.all()
    info_postres = {'postres': mis_postres}
    return render(request, "AppWeb/postre.html", info_postres)


def carta(request):
    return render(request, "AppWeb/carta.html")

def pedido(request):
    return render(request, "AppWeb/pedido.html")

#vistas para los formularios de agregar

def agregarComida(request):

    if request.method == 'POST':
        nueva_comida = ComidaForm(request.POST)
        if nueva_comida.is_valid():
            info = nueva_comida.cleaned_data
            comida_nueva = Comida(nombre=info['nombre'], descripcion=info['descripcion'], precio=info['precio'])
            comida_nueva.save()
            return render(request, "AppWeb/inicio.html")
    else: 
        nueva_comida = ComidaForm()
    return render(request, "AppWeb/agregarComida.html", {'formu_c':nueva_comida})

def agregarBebida(request):
    
        if request.method == 'POST':
            nueva_bebida = BebidaForm(request.POST)
            if nueva_bebida.is_valid():
                info = nueva_bebida.cleaned_data
                bebida_nueva = Bebida(nombre=info['nombre'], descripcion=info['descripcion'], precio=info['precio'])
                bebida_nueva.save()
                return render(request, "AppWeb/inicio.html")
        else: 
            nueva_bebida = BebidaForm()
        return render(request, "AppWeb/agregarBebida.html", {'formu_b':nueva_bebida})

def agregarGuarnicion(request):
    
        if request.method == 'POST':
            nueva_guarnicion = GuarnicionForm(request.POST)
            if nueva_guarnicion.is_valid():
                info = nueva_guarnicion.cleaned_data
                guarnicion_nueva = Guarnicion(nombre=info['nombre'], descripcion=info['descripcion'], precio=info['precio'])
                guarnicion_nueva.save()
                return render(request, "AppWeb/inicio.html")
        else: 
            nueva_guarnicion = GuarnicionForm()
        return render(request, "AppWeb/agregarGuarnicion.html", {'formu_g':nueva_guarnicion})

def agregarPostre(request):
    
        if request.method == 'POST':
            nuevo_postre = PostreForm(request.POST)
            if nuevo_postre.is_valid():
                info = nuevo_postre.cleaned_data
                postre_nuevo = Postre(nombre=info['nombre'], descripcion=info['descripcion'], precio=info['precio'])
                postre_nuevo.save()
                return render(request, "AppWeb/inicio.html")
        else: 
            nuevo_postre = PostreForm()
        return render(request, "AppWeb/agregarPostre.html", {'formu_p':nuevo_postre})


#Vistas para los formularios de busqueda:
