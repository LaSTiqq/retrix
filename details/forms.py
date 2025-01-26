from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Vārds'), widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent mb-2', 'placeholder': _('Jānis'), 'autocomplete': 'off', 'maxlength': '15'}),
        min_length=5)
    sender = forms.EmailField(label=_('E-pasts'), widget=forms.EmailInput(attrs={
        'class': 'form-control bg-transparent mb-2', 'placeholder': _('janis.celotajs@gmail.com'), 'autocomplete': 'off', }))
    subject = forms.CharField(label=_('Temats'), widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent mb-2', 'placeholder': _('LED gaismas virtuvē'), 'autocomplete': 'off', 'maxlength': '30'}),
        min_length=5)
    content = forms.CharField(label=_('Teksts'), widget=forms.Textarea(attrs={
        'class': 'form-control bg-transparent pt-3', 'placeholder': _('Vēlos izgaismot virtuvi, ko Jūs varat piedāvāt?'), 'autocomplete': 'off', 'rows': 6}),
        min_length=50)
    captcha = ReCaptchaField(
        label='Captcha',
        widget=ReCaptchaV3(
            attrs={
                'data-sitekey': settings.RECAPTCHA_PUBLIC_KEY,
            },
            api_params={
                'hl': _('lv'),
            },
        ),
    )
