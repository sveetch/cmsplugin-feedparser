.. _Django: https://www.djangoproject.com/
.. _DjangoCMS: https://www.django-cms.org
.. _django-feedparser: https://github.com/sveetch/django-feedparser

====================
cmsplugin-feedparser
====================

`django-feedparser`_ plugin for DjangoCMS

.. Warning::
    Version 0.3.0 has dropped support for ``DjangoCMS<=3.3.1``.

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/cmsplugin-feedparser>`_;
* Clone it on his `repository <https://github.com/sveetch/cmsplugin-feedparser>`_;

Requires
********

* Django >= 1.8;
* `DjangoCMS`_ >= 3.3.1;
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

Finally install plugin models in your database using migrations: ::

    python manage.py migrate

.. Note::
    Note than since version ``0.2.0``, this plugin has moved to Django migrations system, previous South migration will be freezed in their current state and have been moved to ``south_migrations`` directory as recommended since `South 1.0.x <http://south.readthedocs.org/en/latest/releasenotes/1.0.html>`_.
