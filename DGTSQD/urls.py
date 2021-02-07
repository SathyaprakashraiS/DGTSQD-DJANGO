"""DGTSQD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from main.views import comment
from django.conf.urls.static import static
from main.views import newspost
from main.views import eventpost
from main.views import profile
from main.views import addachievements
from main.views import DispProfile
import os
from main.views import viewprofile

from main.views import viewprofile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('basic/',include("main.urls")),
    path('comment/',include("main.urls")),
    path('',include("django.contrib.auth.urls")),
    path('register/',include("main.urls")),
    path('profile/',include("main.urls")),
    path('',include("django.contrib.auth.urls")),
    path('addachievements/',include("main.urls")),
    path('viewprofile/',include("main.urls")),
    path('dispprofile/',include("main.urls")),
    path('viewprofile/<tager>/',include("main.urls")),
]
#urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)