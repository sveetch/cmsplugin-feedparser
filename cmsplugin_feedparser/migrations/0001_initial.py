# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedparserPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('renderer', models.CharField(default=b'basic-xml', help_text='Feed renderer, your feed must be compatible with it', max_length=100, verbose_name='renderer', choices=[(b'basic-json', b'basic-json'), (b'basic-xml', b'basic-xml')])),
                ('template', models.CharField(help_text='Template used to render the feed', max_length=100, verbose_name='template', choices=[(b'django_feedparser/basic_feed_renderer.html', b'Default template')])),
                ('expiration', models.PositiveIntegerField(default=0, help_text='Cache expiration time until the feed is fetched again, in seconds', verbose_name='expiration')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
