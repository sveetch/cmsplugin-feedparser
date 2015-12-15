"""
Settings for django-feedparser plugin for DjangoCMS
"""
from django_feedparser.settings import FEED_RENDERER_DEFAULT_TEMPLATE

FEED_PLUGIN_TEMPLATE_CHOICES = (
    (FEED_RENDERER_DEFAULT_TEMPLATE, 'Default template'),
)
