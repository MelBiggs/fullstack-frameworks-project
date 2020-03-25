from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def face_products(request):
    products = Product.objects.all().filter(category='F')
    return render(request, "products.html", {"products": products})


def body_products(request):
    products = Product.objects.all().filter(category='B')
    return render(request, "products.html", {"products": products})
