from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput

class ContactForm(forms.Form):
    name = forms.CharField(label='Vārds', widget=forms.TextInput(attrs={'class': 'form-control  mt-2 mx-auto', 'placeholder': 'Vārds/имя/name',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    sender = forms.CharField(label='E-pasts', widget=forms.EmailInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': 'E-pasts/почта/email',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    subject = forms.CharField(label='Temats', widget=forms.TextInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': 'Temats/тема/topic',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    content = forms.CharField(label='Teksts', widget=forms.Textarea(attrs={'class': 'form-control mt-2 mx-auto', 'rows': 5, 'placeholder': 'Teksts/текст/text',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    captcha = CaptchaField(label='Captcha', widget=CaptchaTextInput(attrs={'class': 'form-control d-block mx-auto', 'placeholder': 'Atbilde/ответ/answer'}))