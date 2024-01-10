from django.urls import path
from AppWeb.views import *

urlpatterns = [
    path('', inicio),
    path('inicio/', inicio),
    path('bebida/', bebida),
    path('comida/', comida),
    path('postre/', postre),
    path('carta/', carta),
    path('pedido/', pedido),
]
