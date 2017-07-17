from django import forms
from django.core.exceptions import ValidationError

#from siteLogic.models import behaviouralExperiment, shareBehaviouralExperiment
#
#
#class behaviouralExperimentForm(forms.ModelForm):
#
#    #This is added in case we want to have an extra field that was not available in the models.py description
#    #confirm_email = forms.EmailField(
#    #    label="Confirm email",
#    #    required=True,
#    #)
#
#    class Meta:
#        model = behaviouralExperiment
#    #GE: This excludes model fields from being shown in the form. We are filling creator value from request.user in view.py,
#    #so it doesn't make much sense to show this field to the user
#        exclude = ('creator','users_with_access')
#
#    #This is added in case we want to have an extra field that was not available in the models.py description
#    #See http://effectivedjango.com/tutorial/forms.html# for more information
#    #def __init__(self, *args, **kwargs):
#    #
#    #    if kwargs.get('instance'):
#    #        email = kwargs['instance'].email
#    #        kwargs.setdefault('initial', {})['confirm_email'] = email
#    #
#    #    return super(behaviouralExperimentForm, self).__init__(*args, **kwargs)  
#
#

class support_request_form (forms.Form):
    name = forms.CharField(label='Your name', max_length=100, help_text='100 characters max.')
    email = forms.EmailField(help_text='A valid email address, please.')
    subject = forms.CharField(label='Your name', max_length=100, help_text='100 characters max.')
    body = forms.CharField(label='Your name', max_length=2000,widget=forms.Textarea, help_text='2000 characters max.')