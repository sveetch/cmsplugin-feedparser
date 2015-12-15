"""
Feedparser' DjangoCMS plugins
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django_feedparser.utils import FeedparserError, get_feed_renderer

from .models import FeedparserPluginModel

class FeedparserPluginBase(CMSPluginBase):
    module = 'Feedparser'

class FeedPlugin(FeedparserPluginBase):
    """
    Standard plugin to render a feed
    """
    model = FeedparserPluginModel
    name = _('Feed')
    fields = ('url', 'renderer', 'template', 'expiration')
    render_template = settings.FEED_RENDERER_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        """
        Build feed context using given paramaters and let the plugin render 
        itself with right context
        """
        # Adjust template to the given one
        self.render_template = instance.template
        
        context.update({
            'instance': instance,
        })
        
        renderer = get_feed_renderer(settings.FEED_RENDER_ENGINES, instance.renderer)
        feed_context = renderer().get_context(
            instance.url,
            expiration=instance.expiration,
        )
        context.update(feed_context)
        
        return context

plugin_pool.register_plugin(FeedPlugin)
