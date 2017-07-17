#-*- coding: utf-8 -*-

from django.dispatch import Signal


topic_private_post_create = Signal(providing_args=['topics_private', 'comment'])
topic_private_access_pre_create = Signal(providing_args=['topic', 'user'])