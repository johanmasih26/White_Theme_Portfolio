from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    return render(request,'index.html')


def sendmail(request):
    if request.method == "POST":
        template = render_to_string('email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],  
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['johnbhatti26@gmail.com']
        )
        email.fail_silently = False
        email.send()
        # name = request.POST['name']
        # subject = request.POST['subject']
        # email_from = request.POST['email']
        # message = request.POST['message']
        
    return HttpResponse('sent success')


# recipient_list = ['johnbhatti26@gmail.com']
# send_mail( subject, message, email_from, recipient_list )
        