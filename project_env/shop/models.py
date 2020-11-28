from django.db import models
from blog.models import ArticleBase


class ProductCategory(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Product(ArticleBase):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sells = models.IntegerField(default=0)
    starts = models.IntegerField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


class Messages(models.Model):
    first_name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.subject