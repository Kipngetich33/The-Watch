from django import forms
from . models import Business, User_Profile, Post , Neighborhood
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm): 
    '''
    class that creates a post object create form
    '''
    class Meta:
        model = Post
        fields = ['title','post']

class BusinessForm(forms.ModelForm): 
    '''
    class that creates a new business creation form
    '''
    class Meta:
        model = Business
        fields = ['business_name','business_email','business_description']

class ProfileForm(forms.ModelForm): 
    '''
    class that creates a new business creation form
    '''
    class Meta:
        model = User_Profile
        fields = ['name','neighborhood_id','email']