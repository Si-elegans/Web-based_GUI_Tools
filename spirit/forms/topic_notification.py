#-*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from spirit.models.topic_notification import TopicNotification


class NotificationForm(forms.ModelForm):

    is_active = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = TopicNotification
        fields = ['is_active', ]


class NotificationCreationForm(NotificationForm):

    def __init__(self, user=None, topic=None, *args, **kwargs):
        super(NotificationCreationForm, self).__init__(*args, **kwargs)
        self.user = user
        self.topic = topic

    def clean(self):
        cleaned_data = super(NotificationCreationForm, self).clean()

        notification = TopicNotification.objects.filter(user=self.user,
                                                        topic=self.topic)

        if notification.exists():
            # Do this since some of the unique_together fields are excluded.
            raise forms.ValidationError(_("This notification already exists"))

        return cleaned_data

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.user = self.user
            self.instance.topic = self.topic

        return super(NotificationCreationForm, self).save(commit)