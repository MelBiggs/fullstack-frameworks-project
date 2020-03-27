from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

ITEMS_PER_PAGE = 3

def all_products(request):
    products = Product.objects.all()

    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)

    return render(request, "products.html", {"products": products})


def face_products(request):
    products = Product.objects.all().filter(category='F')
    return render(request, "products.html", {"products": products})


def body_products(request):
    products = Product.objects.all().filter(category='B')
    return render(request, "products.html", {"products": products})


def product_detail(request, pk):
    """
    Create a view that returns a single
    Product object based on the product ID (pk) and
    render it to the 'productdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product': product})


# @login_required
# def like_product(request):



# def filter_tags(request):
