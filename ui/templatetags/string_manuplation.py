from django import template

register = template.Library()


@register.filter(name='capitilize')
def capitilize(value):
    value = value.replace('_', ' ')

    return value[0].upper() + value[1:]