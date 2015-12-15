"""
Models of django-feedparser plugin for DjangoCMS
"""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

RENDERER_CHOICES = tuple([(k, k) for k,v in settings.FEED_RENDER_ENGINES.items()])

class FeedparserPluginModel(CMSPlugin):
    """
    Plugin config to display a feed with django-feedparser
    """
    url = models.CharField(_('url'), max_length=255, blank=False)
    
    renderer = models.CharField(_('renderer'),
        max_length=100,
        choices=RENDERER_CHOICES,
        blank=False,
        default=settings.FEED_DEFAULT_RENDERER_ENGINE,
        help_text=_("Feed renderer, your feed must be compatible with it"),
    )
    
    template = models.CharField(_('template'),
        max_length=100,
        choices=settings.FEED_PLUGIN_TEMPLATE_CHOICES,
        blank=False,
        help_text=_("Template used to render the feed"),
    )
    
    expiration = models.PositiveIntegerField(_('expiration'),
        default=0,
        blank=False,
        help_text=_("Cache expiration time until the feed is fetched again, in seconds"),
    )

    def __unicode__(self):
        return self.url
