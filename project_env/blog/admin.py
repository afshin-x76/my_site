from django.contrib import admin
from .models import PostCategory, Post, ProductCategory, Product


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Post)
admin.site.register(PostCategory)
