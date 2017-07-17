#-*- coding: utf-8 -*-

import hashlib
import os

from markdown import Markdown

from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.image import Image

from spirit.models.comment import Comment
from spirit.models.topic import Topic
from spirit import utils
from django.core.files.storage import default_storage as storage


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', ]

    def __init__(self, user=None, topic=None, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.user = user
        self.topic = topic
        self.mentions = None  # {username: User, }
        self.fields['comment'].widget.attrs['placeholder'] = _("Write comment...")

    def _get_comment_html(self):
        markdown = Markdown(output_formats='html5',
                            safe_mode='escape',
                            extensions=settings.ST_MARKDOWN_EXT)
        markdown.mentions = {}
        comment_html = markdown.convert(self.cleaned_data['comment'])
        self.mentions = markdown.mentions
        return comment_html

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.user = self.user
            self.instance.topic = self.topic

        self.instance.comment_html = self._get_comment_html()
        return super(CommentForm, self).save(commit)


class CommentMoveForm(forms.Form):

    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), widget=forms.TextInput)

    def __init__(self, topic, *args, **kwargs):
        super(CommentMoveForm, self).__init__(*args, **kwargs)
        self.fields['comments'] = forms.ModelMultipleChoiceField(queryset=Comment.objects.filter(topic=topic),
                                                                 widget=forms.CheckboxSelectMultiple)

    def save(self):
        comments = self.cleaned_data['comments']
        comments_list = list(comments)
        topic = self.cleaned_data['topic']
        comments.update(topic=topic)
        return comments_list


class CommentImageForm(forms.Form):

    image = forms.ImageField()

    def __init__(self, user=None, *args, **kwargs):
        super(CommentImageForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_image(self):
        image = self.cleaned_data["image"]

        if Image.open(image).format.lower() not in settings.ST_ALLOWED_UPLOAD_IMAGE_FORMAT:
            raise forms.ValidationError(_("Unsupported file format. Supported formats are %s."
                                          % ", ".join(settings.ST_ALLOWED_UPLOAD_IMAGE_FORMAT)))

        image.seek(0)
        return image

    def save(self):
        image = self.cleaned_data["image"]
        hash = hashlib.md5(image.read()).hexdigest()
        name, ext = os.path.splitext(image.name)

        # Remove the extension if not allowed
        if ext and ext[1:].lower() not in settings.ST_ALLOWED_UPLOAD_IMAGE_EXT:
            ext = ""

        image.name = u"".join((hash, ext.lower()))
        upload_to = os.path.join('spirit', 'images', str(self.user.pk))        
        url_media_ondoren = os.path.join(upload_to, image.name).replace("\\", "/")        
        image.url = os.path.join(settings.MEDIA_URL, upload_to, image.name).replace("\\", "/")        
        media_path = os.path.join(settings.MEDIA_ROOT, upload_to)               
        
        
        file = storage.open(url_media_ondoren, 'wb')
        image.seek(0)
        file.write(image.read())
        file.close()
        image.close()        
        

        return image