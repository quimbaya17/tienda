from django import forms
from .models import Producto 

class ContactoForm(forms.Form):
    correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico'}))
    titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Título'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Texto'}))

class agregar_producto_form(forms.ModelForm):
        class Meta:
              model = Producto
              fields = ['nombre',  'precio', 'stock', 'categorias', 'descripcion']#'__all__'
              exclude = ['foto', ]