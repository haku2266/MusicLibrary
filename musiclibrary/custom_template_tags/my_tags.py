from django import template

register = template.Library()


@register.filter(name='length_query')
def length_query(query):
    l = 0
    for i in query:
        l += 1
    return l
