from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class ProductCategory(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class ArticleBase(models.Model):
    """
    this is base of posts and product
    """
    thumbnail = models.ImageField()
    title = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField()
    content = RichTextField()
    comment = models.IntegerField(default=5)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(ArticleBase):
    price = models.IntegerField(default=0)
    sells = models.IntegerField(default=0)
    starts = models.IntegerField()
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(ProductCategory)


class Post(ArticleBase):
    view = models.IntegerField()
    like = models.BooleanField(default=False)
    category = models.ManyToManyField(PostCategory)
