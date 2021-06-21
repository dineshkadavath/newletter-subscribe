from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views import View
from . import templates
from .models import Newsletter
import json

# mail
import smtplib
from django.core.mail import EmailMessage
        
class HomeHandler(View):
    def get(self, request):
        return render(request, "home.html", {'home':'active'})

class NewsletterHandler(View):
    def get(self, request):
        return render(request, "newsletter_form.html", {})
    
    def post(self, request):
        data = self.request.POST
        username = data.get("name")
        email = data.get("mail")
        print(email)
        subscribe = data.get("subscribe")
        entity = Newsletter()
        entity.name = username
        entity.email = email
        if subscribe == 'on':
            entity.subscribe = True 
        else:
            entity.subscribe = False
        entity.save()
        self.send_email(name=username,email=email)
        return HttpResponse("User Subscription has saved.")

    def send_email(self, name, email):
        head="Newsletter-subscription"
        subject="Hi "+name+",You have subscribed for the newsletter."
        print(head)
        print(subject)
        semail = EmailMessage(str(head),str(subject), to=[email])
        semail.send()


    def recaptcha_check(self, request):
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': '6Lcn9kkbAAAAALx485ismEC3O83yl3LNY4ZJmdpr',
            'response': recaptcha_response
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = json.load(response)
        print(result)

class DashboardHandler(View):
    def get(self, request):
        print("dashboard")
        all_users = Newsletter.objects.all()
        return render(request, "dashboard.html", {"users":all_users})
