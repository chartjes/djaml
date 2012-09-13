"""
Template tags to render HAML strings with HamlPy.
"""

from django.template import Library
from hamlpy import hamlpy

register = Library()
hamlParser = hamlpy.Compiler()


@register.filter
def render_haml(source):
	"""
	.. function render_haml(source)

	Renders *source* string as HAML with HamlPy.
	"""
	return hamlParser.process(source)
