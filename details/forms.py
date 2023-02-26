from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control  mt-2 mx-auto', 'placeholder': 'Vārds | Name | Имя',
																			'autocomplete': 'off', 'required': True}))
    sender = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': 'e-pasts | email | почта',
																			'autocomplete': 'off', 'required': True}))
    subject = forms.CharField(label='Topic', widget=forms.TextInput(attrs={'class': 'form-control mt-2 mx-auto', 'placeholder': 'Temats | Topic | Тема',
																			'autocomplete': 'off', 'required': True}))
    content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control mt-2 mx-auto', 'rows': 5, 'placeholder': 'Teksts | Text | Текст',
																			'autocomplete': 'off', 'required': True}))