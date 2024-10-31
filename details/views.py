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
    url_pattern = re.compile(
        r'https?://(?:[a-zA-Z0-9]|[.!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    restricted_keywords = ["whatsapp", "telegram", "tg", "телеграм", "телега", "тг", "viber", "вайбер",
                           "discord", "дискорд", "аська", "icq", "porn", "loli", "xxx", "cp", "skype", "скайп",
                           "rub", "рублей", "руб", "eur", "dollars", "bonus", "free", "gift", "order now",
                           "spam", "website", "visit our", "earn", "congratulations", "don't miss", "buy now",
                           "limited time", "exclusive offer", "act fast", "special deal", "discount", "sale",
                           "promotion", "pharmacy", "election", "price"]

    has_link = bool(re.search(url_pattern, text))
    has_restricted_keyword = any(re.search(
        r'\b' + re.escape(keyword) + r'\b', text, flags=re.IGNORECASE) for keyword in restricted_keywords)

    return has_link or has_restricted_keyword


def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            if any(restricted_found(form.cleaned_data[field]) for field in ['name', 'subject', 'content']):
                messages.warning(
                    request, _("Jūs ievadījāt kaut ko neatļautu! Mēģiniet vēlreiz."))
                return redirect(_('/#communication'))
            html_content = render_to_string('email.html', {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content']
            })
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
                messages.success(request, _("Vēstule nosūtīta"))
                return redirect(_('/#communication'))
            except SMTPException:
                messages.error(
                    request, _("Radās kļūda! Mēģiniet vēlreiz."))
                return redirect(_('/#communication'))
        else:
            messages.error(
                request, _("Google domā, ka Jūs neesat cilvēks! Mēģiniet vēlreiz."))
            return redirect(_('/#communication'))
    else:
        form = ContactForm()
    return render(request, 'index.html', {"form": form})
