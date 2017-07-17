#-*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from spirit.managers.category import CategoryManager
from spirit.utils.models import AutoSlugField


class Category(models.Model):

    parent = models.ForeignKey('self', verbose_name=_("category parent"), null=True, blank=True)

    title = models.CharField(_("title"), max_length=75)
    slug = AutoSlugField(populate_from="title", db_index=False, blank=True)
    description = models.CharField(_("description"), max_length=255, blank=True)
    is_closed = models.BooleanField(_("closed"), default=False)
    is_removed = models.BooleanField(_("removed"), default=False)
    is_private = models.BooleanField(_("private"), default=False)

    #topic_count = models.PositiveIntegerField(_("topic count"), default=0)

    objects = CategoryManager()

    class Meta:
        app_label = 'spirit'
        ordering = ['title', ]
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def get_absolute_url(self):
        return reverse('spirit:category-detail', kwargs={'pk': str(self.id), 'slug': self.slug})

    @property
    def is_subcategory(self):
        if self.parent_id:
            return True
        else:
            return False

    def __unicode__(self):
        if self.parent:
            return "%s, %s" % (self.parent.title, self.title)
        else:
            return self.title


#def topic_posted_handler(sender, topic, **kwargs):
#    if topic.category.is_subcategory:
#        category = Category.objects.filter(pk__in=[topic.category.pk, topic.category.parent.pk])
#    else:
#        category = Category.objects.filter(pk=topic.category.pk)
#
#    category.update(topic_count=F('topic_count') + 1)


#topic_posted.connect(topic_posted_handler, dispatch_uid=__name__)