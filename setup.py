__doc__ = """
Djaml is a template loader for Django that allows you to use HamlPy for markup.
"""
from setuptools import setup

setup(
    name='djaml',
    version='1.0',
    author='Chris Hartjes',
    description=('A Django template loader for loading and converting '
                 'HamlPy markup to HTML'),
    license='MIT',
    keywords='django haml hamlpy',
    url='http://github.com/chartjes/djaml/',
    packages=['djaml'],
    long_description=__doc__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
