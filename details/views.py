from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm

def send(request):
    form = ContactForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content'],
            }
            html_content = render_to_string('email.html', {
                                            'name': body['name'], 'sender': body['sender'], 'content': body['content']})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                form.cleaned_data['subject'],
                text_content,
                'affixsia@gmail.com',
                ['affixsia@inbox.lv']
            )
            email.attach_alternative(html_content, 'text/html')
            email.send()
            if email:
                messages.success(request, 'Vēstule nosūtīta')
                return redirect('/#contact_us')
            else:
                messages.warning(
                    request, 'Kaut kas nav izdevies, mēģiniet vēlreiz')
                return redirect('/#contact_us')
        else:
            messages.warning(request, 'Atbilde nav pareiza, mēģiniet vēlreiz')
            return redirect('/#contact_us')
    else:
        form = ContactForm()
    return render(request, 'details/index.html', {"form": form})