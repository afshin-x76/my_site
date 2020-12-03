from django.urls import path, re_path, include
from .views import (index, about, products, post_create, post_update,
                    contact, signup, login, logout, posts, post_detail, post_delete)


urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('accounts/signup/', signup, name="signup"),
    path('accounts/login/', login, name="login"),
    path('accounts/logout/', logout, name="logout"),
    path('posts/', posts, name='posts'),
    path('post-create/', post_create, name="post-create"),
    path('post/<pk>/', post_detail, name="post-detail"),
    path('post/<pk>/update/', post_update, name="post-update"),
    path('post/<pk>/delete', post_delete, name="post-delete"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]