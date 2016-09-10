# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Required migration since DjangoCMS==3.3.1 see:

    https://github.com/divio/django-cms/issues/5550
    """
    dependencies = [
        ('cmsplugin_feedparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedparserpluginmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_feedparser_feedparserpluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
