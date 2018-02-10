from django.shortcuts import render
from .email import send_welcome_email

def landing(request):
    return render(request,'landing.html')

