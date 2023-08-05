from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
import re


def restricted_found(text):
    url_pattern = r"(?:http[s]?://|www\.)[^\s/$.?#].[^\s]*"
    restricted_keywords = ["WhatsApp", "whatsapp", "Telegram", "telegram", "tg", "Телеграм", "телеграм", "тг", "Телега", "телега",
                           "Discord", "discord", "Дискорд", "дискорд", "Viber", "viber", "Вайбер", "вайбер", "Аська", "аська", "icq", "ICQ",
                           "Skype", "skype", "Скайп", "скайп", "рублей", "rub", "RUB", "Bonus", "bonus", "Free", "free", "Gift", "gift",
                           "Order now", "order now", "Spam", "spam", "Website", "website", "Visit our", "visit our", "Earn", "earn"]

    has_link = bool(re.search(url_pattern, text))
    has_restricted_keyword = any(
        keyword in text for keyword in restricted_keywords)

    return has_link or has_restricted_keyword


def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content'],
            }
            if restricted_found(body['content']):
                messages.warning(
                    request, _("Jūs ievadījāt kaut ko neatļautu! Ziņa nav nosūtīta"))
                return redirect('/#communication')
            html_content = render_to_string('email.html', {
                                            'name': body['name'], 'sender': body['sender'], 'content': body['content']})
            text_content = strip_tags(html_content)
            try:
                email = EmailMultiAlternatives(
                    form.cleaned_data['subject'],
                    text_content,
                    settings.EMAIL_HOST_USER,
                    ['retrixsia@gmail.com']
                )
                email.attach_alternative(html_content, 'text/html')
                email.send()
                messages.success(request, _('Vēstule nosūtīta'))
                return redirect('/#communication')
            except SMTPException:
                messages.danger(request, _('Radās kļūda, mēģiniet vēlreiz'))
                return redirect('/#communication')
    else:
        form = ContactForm()
    return render(request, 'index.html', {"form": form})
