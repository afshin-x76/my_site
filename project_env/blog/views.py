from django.shortcuts import render, reverse
from shop.models import Product, ProductCategory, Messages
from users.forms import CreateUserForm, UserLoginForm
from django.contrib.auth import logout as my_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as my_login
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Messages.objects.create(first_name=name, email=email, subject=subject, message=message)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'contact.html', {})


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        print("is in post section")
        if form.is_valid():
            print("is in valid")

            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)
    

def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            my_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


def logout(request):
    my_logout(request)
    return HttpResponseRedirect(reverse('index'))


