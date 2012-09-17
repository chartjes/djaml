"""
Template tags to render HAML strings with HamlPy.
"""

from django.template import Library
from django.utils.safestring import mark_safe
from hamlpy import hamlpy

register = Library()
hamlParser = hamlpy.Compiler()


@register.filter
def render_haml(source):
	"""
	.. function render_haml(source)

	Renders *source* string as HAML with HamlPy.
	"""
	return mark_safe(hamlParser.process(source))
