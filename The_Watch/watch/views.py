from django.shortcuts import render
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required.

@login_required(login_url='/accounts/login/')
def landing(request):
    return render(request,'landing.html')

