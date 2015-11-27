from django.shortcuts import render
from .models import Producto,Compra
from django.shortcuts import render, get_object_or_404
from .forms import ProductoForm, CompraForm
from django.shortcuts import redirect
from django.shortcuts import redirect

# Create your views here.
def ver_producto(request):
    productos = Producto.objects.order_by('nombre')
    return render(request, 'carrito/listado_productos.html', {'productos':productos})

def detalle_producto(request,pk):
    producto=get_object_or_404(Producto, pk=pk)
    return render(request, 'carrito/detalle_producto.html', {'producto': producto})

def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('carrito.views.detalle_producto', pk=post.pk)
    else:
        form = ProductoForm()
    return render(request, 'carrito/editar_producto.html', {'form': form})

def editar_producto(request, pk):
        post = get_object_or_404(Producto, pk=pk)
        if request.method == "POST":
            form = ProductoForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('carrito.views.detalle_producto', pk=post.pk)
        else:
            form = ProductoForm(instance=post)
        return render(request, 'carrito/editar_producto.html', {'form': form})


def ver_compra(request):
    compras = Compra.objects.order_by('cliente')
    return render(request, 'carrito/listado_compras.html', {'compras':compras})

def detalle_compra(request,pk):
    compra=get_object_or_404(Compra, pk=pk)
    return render(request, 'carrito/detalle_compra.html', {'compra': compra})

def compra_nueva(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('carrito.views.detalle_compra', pk=post.pk)
    else:
        form = CompraForm()
    return render(request, 'carrito/editar_compra.html', {'form': form})

def editar_compra(request, pk):
        post = get_object_or_404(Compra, pk=pk)
        if request.method == "POST":
            form = CompraForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('carrito.views.detalle_compra', pk=post.pk)
        else:
            form = CompraForm(instance=post)
        return render(request, 'carrito/editar_compra.html', {'form': form})
