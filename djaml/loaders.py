from django.template import TemplateDoesNotExist

from hamlpy import hamlpy

from utils import get_django_template_loaders

def get_haml_loader(loader):
    if hasattr(loader, 'Loader'):
        baseclass = loader.Loader
    else:
        class baseclass(object):
            def load_template_source(self, *args, **kwargs):
                return loader.load_template_source(*args, **kwargs)

    class Loader(baseclass):
        def load_template_source(self, template_name, *args, **kwargs):
            if not template_name.endswith('.haml'):
                raise TemplateDoesNotExist(template_name)
            
            haml_source, template_path = super(Loader, self).load_template_source(template_name, *args, **kwargs)
            hamlParser = hamlpy.Compiler()
            html = hamlParser.process(haml_source)
            
            return html, template_path

        load_template_source.is_usable = True

    return Loader

haml_loaders = dict((name, get_haml_loader(loader))
        for (name, loader) in get_django_template_loaders())

