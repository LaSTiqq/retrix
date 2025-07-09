from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Vārds'), widget=forms.TextInput(attrs={
        'id': 'name', 'value': _('Jānis'), 'class': 'form-control bg-transparent', 'placeholder': _('Vārds'), 'autocomplete': 'off', 'maxlength': '15'}),
        min_length=3)
    email = forms.EmailField(label=_('E-pasts'), widget=forms.EmailInput(attrs={
        'id': 'email', 'value': _('janis.celotajs@gmail.com'), 'class': 'form-control bg-transparent', 'placeholder': _('E-pasts'), 'autocomplete': 'off', }))
    subject = forms.CharField(label=_('Temats'), widget=forms.TextInput(attrs={
        'id': 'subject', 'value': _('Apgaismojums virtuvē'), 'class': 'form-control bg-transparent', 'placeholder': _('Temats'), 'autocomplete': 'off', 'maxlength': '30'}),
        min_length=5)
    message = forms.CharField(label=_('Ziņojums'), widget=forms.Textarea(attrs={
        'id': 'message', 'class': 'form-control bg-transparent', 'placeholder': _('Ziņojums'), 'autocomplete': 'off'}),
        min_length=20)
