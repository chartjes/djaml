Djaml is a template loader for Django that allows you to use [HamlPy](https://github.com/jessemiller/HamlPy) in your templates

It is based on the [django-shpaml-template-loader project](http://bitbucket.org/jiaaro/django-shpaml-template-loader),
and is licensed under the MIT license.

## Requirements

* [Django](http://www.djangoproject.org) -- I've tested it using Django 1.2.x, 1.3.0 and the version of Django that is included with the [djangoappengine](http://www.allbuttonspressed.com/projects/djangoappengine) project
* [HamlPy](https://github.com/jessemiller/HamlPy) -- tested using version as of December 4, 2010

## Installation

You can either copy all the files into 'djaml' in the root of your Django project
or install it using the included setup.py file.

Having done that, you need to add djaml as the first item in TEMPLATE_LOADERS

    TEMPLATE_LOADERS = (
        'djaml.loaders.DjamlFilesystemLoader',
        'djaml.loaders.DjamlAppDirectoriesLoader',
        ...
    )

If you don't put djaml first, then the standard Django template loaders will try and process
it first.

Make sure your templates have a .haml extension, and put them wherever you've told Django
to expect to find templates.


## Template caching

Just add `django.template.loaders.cached.Loader` to your TEMPLATE_LOADERS:

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            ...
            'djaml.loaders.DjamlFilesystemLoader',
            'django.template.loaders.filesystem.Loader',
            ...
      )),
    )


## Example

Here's a sample of what a Django layout file looks like using Haml:

    # base.haml
    !!!
    %html
        %head
            %title
                -block title
                    Internet Baseball League
            %meta{'http-equiv': 'Content-Type', content: 'text/html; charset=UTF-8'}/
            %link{rel: 'stylesheet', type: 'text/css', href:'/site_media/css/grid.css'}/
            %link{rel: 'stylesheet', type: 'text/css', href:'/site_media/css/ibl.css'}/
            %script{src: "/site_media/js/modernizr-1.7.min.js"}
        %body
            .row
                #sidebar.column.grid_2
                    %img{src: '/site_media/images/ibl_logo.gif', alt: 'IBL Logo'}<br>
                    #navcontainer
                        %ul#navlist
                            %li
                                %a{href: '{% url home %}'} Home
                            %li
                                %a{href: 'http://archive.ibl.org'} Archive

                #container.column.grid_10
                    - block content
                        Some text for the content


    # one.haml
    -extends 'base.haml'
    -block title
         Another page
    -block content
         .wide More content

         %form{action: '/', method: 'POST'}
            %table
                =vote_form.as_table
            %button Vote!


## Questions or Feedback

If you have any questions or comments, send some email to chartjes@littlehart.net
