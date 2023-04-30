from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from .models import *
from django.contrib import messages


def home(request):
    return render(request,'index.html')

def emailsend(request):
    if request.method=='POST':
        email_to=request.POST.get('email_to')
        print(email_to,'.........')
        email_sub=request.POST.get('email_sub')
        email_body=request.POST.get('email_body')
        email_attachment=request.FILES.get('email_attachment')
        print(email_attachment,'//////////////')
        msg = EmailMessage(email_sub, email_body, settings.EMAIL_HOST_USER, [email_to])
        msg.attach(email_attachment,"application/pdf")
        msg.send()
        messages.success(request,'Successfully!!!')
        return render(request,'index.html')
    else:
        return render(request,'index.html')
