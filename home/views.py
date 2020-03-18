from django.shortcuts import render
from products.models import Product

def index(request):
    """A view that displays the index page"""
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})
