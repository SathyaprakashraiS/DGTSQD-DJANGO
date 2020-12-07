from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
#from django.contrib.auth.forms import UserCreationProfile
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser
from .models import review
from .models import news
from .models import event
from .forms import EventForm
from .forms import ImageForm
from .models import UserProfile
from .forms import EditProfileForm
from .models import project
from .models import achievements
from .forms import EditProfileForm,UserProfileForm,AcheivementForm,ProjectForm
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import report
from .forms import Report
import pil
 
# Create your views here.
def comment(request):
    obj = review.objects.all()
    
    
    return render(request,"review.html",{'obj':obj})


def add_comment(request):
    p = request.GET['head']
    c = request.GET['review']
    review.objects.create(name=p,comment=c)
    return HttpResponseRedirect("/")

def basic(request):
	
    return render(request,"basic.html",{'name':request.user.username})


def pybot(request):
    query = request.GET.get('query')

    
    try:
        client = wolframalpha.Client("<--Your API key-->")
        res = client.query(query)
        ans = next(res.results).text
        return render(request,"pybot.html", {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request,"pybot.html", {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request,"pybot.html", {'ans': ans, 'query': query})

def register(request):
    form = UserCreationForm()
    
    

    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("register/")
      
    
    context = {'form':form}
    return render(request,"register.html",context)

def tmembers(request,tager="1"):
       obj1=UserProfile.objects.get(idcard=1)
       obj2=UserProfile.objects.get(idcard=2)
       obj3=UserProfile.objects.get(idcard=3)
       obj4=UserProfile.objects.get(idcard=4)
       return render(request,"tmembers.html",{'obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4})
      
def aboutus(request):
    return render(request,"aboutus.html")
def contactus(request):
    return render(request,"contactus.html")




def newspost(request):
    obj=news.objects.all()
    return render(request,"newspostdisplay.html",{'obj':obj})

def pproject(request):
    obj=project.objects.all()
    return render(request,"project.html",{'obj':obj})

def newspostupload(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            img_obj = form.instance
            return render(request, 'addpost.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'addpost.html', {'form': form})

def projectupload(request):
  
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            img_obj = form.instance
            return render(request, 'uploadproject.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProjectForm()
    return render(request, 'uploadproject.html', {'form': form})

def addachievements(request):
    if request.method == 'POST':
        form = AcheivementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            img_obj = form.instance
            return render(request, 'addachievements.html', {'form': form, 'img_obj': img_obj})
    else:
        form = AcheivementForm()
    return render(request, 'addachievements.html', {'form': form})

def eventspostupload(request):
  
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            img_obj = form.instance
            return render(request, 'addpostevents.html', {'form': form, 'img_obj': img_obj})
    else:
        form = EventForm()
    return render(request, 'addpostevents.html', {'form': form})

def eventpost(request):
    obj=event.objects.all()
    return render(request,"events.html",{'obj':obj})

def profile(request,tager="1"):
    s=request.GET.get('test')
    #return HttpResponse(s)
    q=UserProfile.objects.get(idcard=s)
    return render(request,"profile.html",{'q':q})

def viewprofile(request):
    
    if request.method == 'POST':
              e_form = EditProfileForm(request.POST,instance=request.user)
              u_form = UserProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        
              if e_form.is_valid() and u_form.is_valid():
                  e_form.save()
                  u_form.save()
                  messages.success(request,f'your account has been updated!')
                  return redirect('dispprofile')
    else:
        e_form = EditProfileForm(instance=request.user)
        u_form = UserProfileForm(instance=request.user.userprofile)    
    context ={
        'e_form':e_form,
        'u_form':u_form
    }
    return render(request,"viewprofile.html",context)   

def members(request):
    obj=UserProfile.objects.all()
    #obj = review.objects.all()
    #return HttpResponse(obj)
    return render(request,"members.html",{'obj':obj})

def newspage(request):
    obj=report.objects.all()
    return render(request,"news.html",{'obj':obj})

def aachievements(request):
    obj=achievements.objects.all()
    return render(request,"achievements.html",{'obj':obj})

def DispProfile(request):
    return render(request,"disp_profile.html")

def reportupload(request):
  
    if request.method == 'POST':
        form = Report(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            img_obj = form.instance
            return render(request, 'reportnews.html', {'form': form, 'img_obj': img_obj})
    else:
        form = Report()
    return render(request, 'reportnews.html', {'form': form}) 

def showinfo(request):
    a=request.GET['image']
    b=request.GET['information']
    return render(request,"showinfo.html",{'a':a,'b':b})


def viewinfo(request,tager="1"):
        a = request.GET.get('info')
        obj = news.objects.all().get(pk = a)
        context = {
            'obj':obj
        }
        return render(request,"viewinfo.html",context)

