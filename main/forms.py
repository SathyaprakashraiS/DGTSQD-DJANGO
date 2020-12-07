from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
#from django.contrib.auth.forms import UserCreationProfile
from django.contrib.auth.models import User
from .models import news,UserProfile,event,project,achievements,report
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = news
       fields = ('info', 'img')

class EventForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = event
       fields = ('info', 'img', 'name')

class Report(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model =report
       fields = ('info','link','img')

class AcheivementForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = achievements
       fields = ('info', 'img')

class ProjectForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = project
       fields = ('title','info','author','img','link')

class UserProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user','idcard']


class EditProfileForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username','email']

def newspage(request):
    obj=report.objects.all()
    return render(request,"news.html",{'obj':obj})