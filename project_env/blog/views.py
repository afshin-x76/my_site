from django.shortcuts import render, reverse, get_object_or_404
from shop.models import Product, ProductCategory, Messages
from users.forms import CreateUserForm, UserLoginForm
from django.contrib.auth import logout as my_logout
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as my_login
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from posts.models import Posts, Comments
from posts.forms import PostCreate, CommentForm
from users.models import CustomUser


def index(request):
    latest_products = Product.objects.order_by("-time_stamp")[:6]
    latest_posts = Posts.objects.order_by("-time_stamp")
    context = {
        'latest_products': latest_products,
        'latest_posts': latest_posts,
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


def posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_create(request):
    form = PostCreate()
    if request.method == 'POST':
        form = PostCreate(request.POST, request.FILES)
        print("is post!!")
        if form.is_valid():
            print("is valid")
            form.instance.owner = request.user
            form.save()
            print("eeeeeeeeeeeeeeeeeeeeee")
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'create-post.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    form = PostCreate(request.POST, request.FILES, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts'))
    return render(request, "create-post.html", {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.writer = request.user
            form.instance.post = post
            form.save()
            return HttpResponseRedirect(reverse('post-detail', args=pk))
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post-detail.html', context)


def post_delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse('posts'))