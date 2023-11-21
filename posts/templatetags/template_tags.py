from django import template

register = template.Library()


@register.simple_tag(name='tab')
def tab(number):
    return number * '    '


@register.simple_tag(name='linebreak')
def linebreak(number):
    return number * '<br>'
