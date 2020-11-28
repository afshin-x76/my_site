from django.shortcuts import render
from shop.models import Product, ProductCategory

def index(request):
    latests = Product.objects.order_by("-time_stamp")[:6]
    context = {
        'latests': latests
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.values_list()
    category_list = []
    for i in categories:
        category_list.append(i[1])
    context = {
        'products': products,
        'categories': category_list
    }
    return render(request, 'products.html', context)


def contact(request):
    return render(request, 'contact.html', {})


