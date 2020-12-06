from django.db import models
from blog.models import ArticleBase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()


class ProductCategory(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


LABEL_CHOICES = [
    ('P','primary'),
    ('s', 'secondary'),
    ('D','danger'),
]
STATE_COICES = [
    ('ASH', 'آذربایجان شرقی'),
    ('AGH', 'آذربایجان غربی'),
    ('ARB', 'اردبیل'),
    ('ES', 'اصفهان'),
    ('AL', 'البرز'),
    ('IL', 'ایلام'),
    ('BSH', 'بوشهر'),
    ('TEH', 'تهران'),
    ('CHKH', 'چهارمحال و بختیاری'),
    ('KHj', 'خراسان جنوبی'),
    ('KHR', 'خراسان رضوی'),
    ('KHSH', 'خراسان شمالی'),
    ('KHZ', 'خوزستان '),
    ('ZNJ', 'زنجان'),
    ('SMN', 'سمنان'),
    ('SB', 'سیستان و بلوچستان'),
    ('FA', 'فارس'),
    ('QHZ', 'قزوین'),
    ('GHOM', 'قم'),
    ('KRD', 'کردستان'),
    ('KRM', 'کرمان'),
    ('KRSH', 'کرمانشاه'),
    ('KGB', 'کهگیلویه و بویراحمد'),
    ('GOL', 'گلستان'),
    ('GIL', 'گیلان'),
    ('LOR', 'لرستان'),
    ('MAZ', 'مازندران'),
    ('MARZ', 'مرکزی'),
    ('HRMZ', 'هرمزگان'),
    ('HMDN', 'همدان'),
    ('YAZD', 'یزد'),
 ]



class Product(ArticleBase):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sells = models.IntegerField(default=0)
    starts = models.IntegerField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')

    def __str__(self):
        return self.title

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", args=[self.pk])


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantinity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user) +':' + str(self.product.title) + ":" + str(self.quantinity)

    def get_total_price(self):
        return self.quantinity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct, related_name="products")
    start_date = models.DateTimeField(auto_now_add=True)
    # ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = 0
        for product in self.products.all():
            total += product.get_total_price()
        return total


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(choices=STATE_COICES, max_length=4, default='TEH')
    address = models.TextField()
    phone_number = models.IntegerField()
    plaque = models.CharField(max_length=10)
    


class Messages(models.Model):
    first_name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.subject