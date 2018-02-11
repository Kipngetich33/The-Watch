from django.shortcuts import render, redirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from . models import User_Profile ,Business ,Neighborhood, Post
from . forms import PostForm, ProfileForm, BusinessForm

@login_required(login_url='/accounts/login/')
def landing(request):
    try:
        current_user = request.user
        current_profile = User_Profile.find_profile_by_id(current_user) 
        current_neighborhood = Neighborhood.find_neighborhood(current_profile.neighborhood_id.id)
        posts = Post.get_all_post()
        
        return render(request,'landing.html',{"current_neighborhood":current_neighborhood,"current_user":current_user, "posts":posts})
    except:
        return redirect(create_profile)

def create_profile(request):
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( landing )
    else:
        form = ProfileForm()
    return render(request,'profile/create_profile.html',{"form":form,})

def business(request):
    current_user = request.user
    current_profile = User_Profile.find_profile_by_id(current_user)
    current_neighborhood = Neighborhood.find_neighborhood(current_profile.neighborhood_id.id)

    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_business = form.save(commit = False)
            new_business.user_id =  current_user
            new_business.neighborhood_id = current_neighborhood
            new_business.save()
            return redirect( landing ) 
    else:
        form = BusinessForm()
    return render(request,'business/business.html',{"form":form})

def view_business(request):
    current_user = request.user
    current_profile = User_Profile.find_profile_by_id(current_user)
    current_neighborhood = Neighborhood.find_neighborhood(current_profile.neighborhood_id.id)
    found_businesses = Business.all_business()
    return render(request,'business/view_business.html',{"current_user":current_user,"found_businesses":found_businesses, "current_profile": current_profile,"current_neighborhood":current_neighborhood})

def post(request):
    current_user = request.user
    current_profile = User_Profile.find_profile_by_id(current_user) 
    current_neighborhood = Neighborhood.find_neighborhood(current_profile.neighborhood_id.id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.user_id =  current_user
            new_post.neighborhood_id = current_neighborhood
            new_post.save()
            return redirect( landing ) 
    else:
        form = PostForm()
    return render(request,'post.html',{"form":form})