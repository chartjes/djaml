from django.template import Library
from hamlpy import hamlpy

register = Library()


@register.filter
def render_haml(source):
    hamlParser = hamlpy.Compiler()
    return hamlParser.process(source)
