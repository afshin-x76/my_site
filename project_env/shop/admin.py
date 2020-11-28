from django.contrib import admin
from .models import Product, ProductCategory, Messages


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Messages)


