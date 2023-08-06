from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import redirect

def add_product(request, product_id):

    carro = Cart(request)
    product = Product.objects.get(id=product_id)
    carro.agregar(product=product)

    return redirect("store")


def delete_product(request, product_id):
    carro = Cart(request)
    product = Product.objects.get(id=product_id)
    carro.eliminar(product=product)

    return redirect("store")


def subtract_product(request, product_id):
    carro = Cart(request)
    product = Product.objects.get(id=product_id)
    carro.restar_producto(product=product)

    return redirect("store")


def clear_cart(request, product_id):
    carro = Cart(request)
    carro.limpiar_carro()

    return redirect("store")