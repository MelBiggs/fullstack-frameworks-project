from django.shortcuts import render
from products.models import Product


PRODUCTS_TO_DISPLAY = 6

def index(request):
    """A view that displays the index page and 6 most recent
    products """
    products = Product.objects.all().order_by('-id')[:PRODUCTS_TO_DISPLAY]
    return render(request, "index.html", {"products": products})
