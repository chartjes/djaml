-*- markdown -*-

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
        'djaml.filesystem',
        'djaml.app_directories',
        ...
    )

If you don't put djaml first, then the standard Django template loaders will try and process
it first.

Make sure your templates have a .haml extension, and put them wherever you've told Django
to expect to find templates.

## Example

Here's a sample of what a Django layout file looks like using Haml:

    <!DOCTYPE html>
    %html
      %head
        %meta{'http-equiv': 'Content-Type', 'content': 'text/html; charset=UTF-8'}
        %title Internet Baseball League
        %link{'rel': 'stylesheet', 'type': 'text/css', 'href':'/site_media/css/grid.css'}
        %link{'rel': 'stylesheet', 'type': 'text/css', 'href':'/site_media/css/ibl.css'}
        %script{'src': "/site_media/js/modernizr-1.7.min.js"}
      %body
        %div{'class': 'row'}
          #sidebar{'class': 'column grid_2'}
            %img{'src': '/site_media/images/ibl_logo.gif', 'alt': 'IBL Logo'}<br>
            #navcontainer
              %ul#navlist
                %li
                  %a{'href': '{% url home %}'} Home
                %li
                  %a{'href': 'http://archive.ibl.org'} Archive
                %li
                  %a{'href': 'http://iblgame.ibl.org'} Cards
                %li
                  %a{'href': 'http://wiki.ibl.org/dokuwiki/doku.php?id=constitution'} Constitution
                %li
                  %a{'href': '{% url free-agents %}'} Free Agents
                %li
                  %a{'href': 'http://wiki.ibl.org/dokuwiki/doku.php?id=owners'} Owners
                %li
                  %a{'href': '/results'} Results
                %li
                  %a{'href': '/rotations'} Rotations
                %li
                  %a{'href': '/schedule'} Schedule
                %li
                  %a{'href': '/standings'} Standings
                %li
                  %a{'href': '/starts'} Starts / Limits
                %li
                  %a{'href': 'http://wiki.ibl.org'} Wiki
                %li

          #container{'class': 'column grid_10'}
            {% block content %}
            {% endblock %}


## Questions or Feedback

If you have any questions or comments, send some email to chartjes@littlehart.net
