from django.utils.translation import gettext_lazy as _
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Vārds'), widget=forms.TextInput(attrs={
        'id': 'name', 'class': 'form-control bg-transparent my-2', 'placeholder': _('Vārds'), 'autocomplete': 'off', 'maxlength': '15'}),
        min_length=3)
    email = forms.EmailField(label=_('E-pasts'), widget=forms.EmailInput(attrs={
        'id': 'email', 'class': 'form-control bg-transparent my-2', 'placeholder': _('E-pasts'), 'autocomplete': 'off', }))
    subject = forms.CharField(label=_('Temats'), widget=forms.TextInput(attrs={
        'id': 'subject', 'class': 'form-control bg-transparent my-2', 'placeholder': _('Temats'), 'autocomplete': 'off', 'maxlength': '30'}),
        min_length=5)
    message = forms.CharField(label=_('Ziņojums'), widget=forms.Textarea(attrs={
        'id': 'message', 'class': 'form-control bg-transparent my-2', 'placeholder': _('Ziņojums'), 'autocomplete': 'off'}),
        min_length=20)
