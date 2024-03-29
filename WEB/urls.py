
"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('login.urls')),
    path("",views.index, name='index'),
    path('', include('file_upload.urls')),
    path('success/', views.success, name='success'),
    path('board/',include('board.urls')),
    path('contact/',views.contact, name='contact'),
    path('search_main/',views.search_main, name='search_main'),
    path('about/', views.about, name='about'),
    
] 
