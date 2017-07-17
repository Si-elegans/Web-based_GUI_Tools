"""
Forms and validation code for user registration.

"""


from django.conf import settings
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

from django import forms
from django.utils.translation import ugettext_lazy as _

from registration.backends import get_module

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}


registration_form_mixin = None
if getattr(settings, 'REGISTRATION_FORMS_MIXIN', None):
    registration_form_mixin = get_module(settings.REGISTRATION_FORMS_MIXIN)

RegistrationFormsMixin = type('RegistrationFormsMixin', (registration_form_mixin or object,), {})


class RegistrationFormFromUserModel(object):
    """
    Create form from django user model
    """
    def __init__(self, *args, **kwargs):
        super(RegistrationFormFromUserModel, self).__init__(*args, **kwargs)
        # add new fields befor exsist sields 
        for field in set([User.USERNAME_FIELD,] + list(User.REQUIRED_FIELDS)):            
            self.fields.update ( {field : User._meta.get_field(field).formfield()})
            


class RegistrationForm(RegistrationFormsMixin, RegistrationFormFromUserModel, forms.Form):
    """
    Form for registering a new user account.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    """

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
        label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
        label=_("Password (again)"))

    #    def clean_username(self):
    #        """
    #        Validate that the username is alphanumeric and is not already
    #        in use.
    #
    #        """
    #        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
    #        if existing.exists():
    #            raise forms.ValidationError(_("A user with that username already exists."))
    #        else:
    #            return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.
    
    """
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
        label=_(u'I have read and agree to the Terms of Service'),
        error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.
    
    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.
    
    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.
    
    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.
        
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']
