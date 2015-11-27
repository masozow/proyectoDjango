from django import forms
from .models import Producto,Compra

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion','precio',)

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ('cod_producto', 'cliente','tarjeta_credito','direccion_entrega','telefonos_cliente',)
