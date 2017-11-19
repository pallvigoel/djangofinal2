# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None
    context = {'title': title, 'form': form}
    
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from my site.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
        form= "none"
        title = "Thanks!"
	confirm_message = "Thanks for the message. We will get right back to you."
    context = {'title': title, 'form': form, 'confirm_message': confirm_message ,}
    return render(request, 'contact.html', context)
