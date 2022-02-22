from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def wiki_parse(value):
    # return value.lower()
    return '<b>bold</b>'