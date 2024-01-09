from django.urls import path
from AppWeb.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('bebidas/', bebida),
    path('comidas/', comida),
    path('postres/', postre),
]
