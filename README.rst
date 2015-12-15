.. _Django: https://www.djangoproject.com/
.. _DjangoCMS: https://www.django-cms.org
.. _django-feedparser: https://github.com/sveetch/django-feedparser

====================
cmsplugin-feedparser
====================

`django-feedparser`_ plugin for DjangoCMS

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/cmsplugin-feedparser>`_;
* Clone it on his `repository <https://github.com/sveetch/cmsplugin-feedparser>`_;

Requires
********

* `DjangoCMS`_ >= 3.0;
* `django-feedparser`_ >= 0.1.2;

Install
*******

First install the package ::

    pip install cmsplugin-feedparser

Add it to your installed Django apps in settings : ::

    INSTALLED_APPS = (
        ...
        'django_feedparser',
        'cmsplugin_feedparser',
        ...
    )

Then import their settings: ::

    from django_feedparser.settings import *
    from cmsplugin_feedparser.settings import *

Finally install app models in your database using Django migrations: ::

    python manage.py migrate
