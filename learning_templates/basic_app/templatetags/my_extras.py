from django import template

register = template.Library()


#另一种注册方法：使用装饰器
@register.filter(name = 'appword')

def append_word(value, arg):

    value = str(value) + str(arg)

    return value



#一种注册方法：
# register.filter('cut', cut)