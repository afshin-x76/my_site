from django import template

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

register.filter('times', times)
register.filter('side', side)
