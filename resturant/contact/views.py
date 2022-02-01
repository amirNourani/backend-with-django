from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact(request):
    sent = False
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            cd = contact.cleaned_data
            name = cd['name']
            email = cd['email']
            subject = cd['subject']
            message = cd['message']
            msg = f'name:{name}\nemail:{email}\nmessage:{message}'
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['amirnurani2001@gmail.com',], fail_silently=False)
            sent = True
    else:
        contact = ContactForm()
        
    context = {
        'contact': contact,
        'sent':sent,
    }
    return render(request, 'contact/contact.html', context)
