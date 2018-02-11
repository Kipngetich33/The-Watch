from django.shortcuts import render
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from . models import User_Profile ,Business ,Neighborhood

@login_required(login_url='/accounts/login/')
def landing(request):
    current_user = request.user
    current_profile = User_Profile.find_profile_by_id(current_user) 
    current_neighborhood = Neighborhood.find_neighborhood(current_profile.neighborhood_id.id)
    return render(request,'landing.html',{"current_neighborhood":current_neighborhood})

