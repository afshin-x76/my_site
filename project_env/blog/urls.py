from django.urls import path
from .views import index, about, products, contact


urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('about', about, name="about"),
    path('contact', contact, name="contact")
    # path('', index),
    
]