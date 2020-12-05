from django import template
from shop.models import Order
register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='side')
def side(number):
    print(number)
    print(type(number))
    a = number % 2 == 0
    print(a)
    return a

@register.filter()
def item_count(user):
    if user.is_authenticated:
        qs = Order.objects.get(user=user)
        return qs.products.count()
    else:
        return 0



register.filter('times', times)
register.filter('side', side)
