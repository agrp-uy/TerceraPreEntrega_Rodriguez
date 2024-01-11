from django import forms

class ComidaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    descripcion = forms.CharField(label='Descripcion', max_length=100)
    precio = forms.IntegerField(label='Precio')

class BebidaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    descripcion = forms.CharField(label='Descripcion', max_length=100)
    precio = forms.IntegerField(label='Precio')

class GuarnicionForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    descripcion = forms.CharField(label='Descripcion', max_length=100)
    precio = forms.IntegerField(label='Precio')

class PostreForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    descripcion = forms.CharField(label='Descripcion', max_length=100)
    precio = forms.IntegerField(label='Precio')

