from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'

def insertar_producto(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre']
        imagen1 = request.POST['imagen1']
        precio = request.POST['precio']
        producto = Producto(id=id, nombre=nombre, imagen1=imagen1, precio=precio)
        producto.save()
        return redirect('listar_productos')

    return redirect('listar_productos')

def modificar_producto(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.imagen1 = request.POST['imagen1']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('listar_productos')
    return render(request, 'modificarproducto.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = Producto.objects.get(id=pk)
    producto.delete()
    return redirect('listar_productos')