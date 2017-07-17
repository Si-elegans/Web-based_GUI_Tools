#-*- coding: utf-8 -*-

from django.dispatch import Signal


comment_posted = Signal(providing_args=['comment', 'mentions'])
comment_pre_update = Signal(providing_args=['comment', ])
comment_post_update = Signal(providing_args=['comment', ])