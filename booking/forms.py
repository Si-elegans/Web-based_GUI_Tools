from django import forms
from booking.models import Reservation

class Reservation_form(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Reservation_form, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['experiment'].widget.attrs['readonly'] = True
    #
    # def clean_sku(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.sku
    #     else:
    #         return self.cleaned_data['experiment']
    class Meta:
        model = Reservation
        fields = ('status', 'error_admin_updates', 'uuid')