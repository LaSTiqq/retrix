from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Vārds'), widget=forms.TextInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': _('Jānis'),
                                                                            'autocomplete': 'off', 'required': True}))
    sender = forms.EmailField(label=_('E-pasts'), widget=forms.EmailInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': _('janis.celotajs@gmail.com'),
                                                                            'autocomplete': 'off', 'required': True}))
    subject = forms.CharField(label=_('Temats'), widget=forms.TextInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': _('LED gaismas virtuvē'),
                                                                            'autocomplete': 'off', 'required': True}))
    content = forms.CharField(label=_('Teksts'), widget=forms.Textarea(attrs={'class': 'form-control mt-2 mx-auto', 'rows': 5, 
                                                                            'placeholder': _('Vēlos izgaismot virtuvi, ko Jūs varat piedāvāt?'),
                                                                            'autocomplete': 'off', 'required': True}))
