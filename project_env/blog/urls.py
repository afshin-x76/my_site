from django.urls import path
from .views import index, about, products, contact, signup, login, logout


urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),

]