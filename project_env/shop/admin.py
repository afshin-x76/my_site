from django.contrib import admin
from .models import Product, ProductCategory, Messages, Order, OrderProduct, BillingAddress


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Messages)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(BillingAddress)




