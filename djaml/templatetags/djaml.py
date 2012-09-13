"""
Template tags to render HAML strings with HamlPy.
"""

from django.template import Library
from hamlpy import hamlpy

register = Library()


@register.filter
def render_haml(source):
	"""
	.. function render_haml(source)

	Renders *source* string as HAML with HamlPy.
	"""
	hamlParser = hamlpy.Compiler()
	return hamlParser.process(source)
