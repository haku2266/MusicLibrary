from django import template
from django.db.models import Count

register = template.Library()


def length_query(query):
    l = 0
    for i in query:
        l += 1
    return l


register.filter('length_query', length_query)


def query_order(arg, n: str):
    return arg.annotate(Count(n)).order_by(f'-{n}__count')


register.filter('query_order', query_order)


def is_inside_query(query, item):
    for i in query:
        if i == item:
            return True
    return False


register.filter('is_inside_query', is_inside_query)


