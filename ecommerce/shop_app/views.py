from django.shortcuts import render, get_object_or_404
from .models import Product
import sqlite3

# Create your views here.
def index(request):
    products = Product.objects.all().order_by('-created_date')[:4]
    return render(request, "index.html", {'products': products})

def cart(request):
    return render(request, "cart.html")

def dashboard(request):
    return render(request, "dashboard.html")

def order_complete(request):
    return render(request, "order_complete.html")

def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    return render(request, 'product-detail.html', {'product': product})

def register(request):
    return render(request, "register.html")

def search_result(request):
    return render(request, "search_result.html")

def signin(request):
    return render(request, "signin.html")

def store(request, category_slug=None):
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    return render(request, "store.html", {'products': products})

def place_order(request):
    return render(request, "place-order.html")