from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class review(models.Model):
	name=models.CharField(max_length=100)
	comment=models.CharField(max_length=5000)

class news(models.Model):
	info=models.CharField(max_length=10000)
	img=models.ImageField(upload_to='images', default='static/images/14358.jpg')
	
class event(models.Model):
	info=models.CharField(max_length=10000)
	img=models.ImageField(upload_to='images', default='static/images/14358.jpg')
	name=models.CharField(max_length=100,default="EVENT")

class achievements(models.Model):
	info=models.CharField(max_length=10000)
	img=models.ImageField(upload_to='images', default='static/images/14358.jpg')

class report(models.Model):
	info=models.CharField(max_length=10000)
	link=models.CharField(max_length=1000,default="NO LINK AVAILABLE")
	img=models.ImageField(upload_to='images', default='static/images/14358.jpg')

class project(models.Model):
	title=models.CharField(max_length=100,default="title")
	info=models.CharField(max_length=5000)
	author=models.CharField(max_length=100)
	img=models.ImageField(upload_to='images', default='static/images/14358.jpg')
	link=models.CharField(max_length=1000,default="NO LINK AVAILABLE")

class UserProfile(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   phone = models.CharField(max_length=256, blank=True, null=True)
   img = models.ImageField(upload_to='images', default='static/images/14358.jpg')
   about = models.CharField(max_length=50000, default='timezone.now')
   idcard=models.CharField(max_length=10,default='100')
   
   def __str__(self):
	   return self.user.username
	     
def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)