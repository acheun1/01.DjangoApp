"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.app_01.urls', namespace="app_01")),          
    url(r'^new', include('apps.app_02.urls', namespace="app_02")),          
    url(r'^create', include('apps.app_03.urls', namespace="app_03")),
    url(r'^([0-9])', include('apps.app_04.urls', namespace="app_04")),
    url(r'^edit/([0-9])', include('apps.app_05.urls', namespace="app_05")),    
    url(r'^delete/([0-9])', include('apps.app_06.urls', namespace="app_06"))    
]
