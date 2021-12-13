"""
xperiencedezignwiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('dezigntools/', include
    ('dezigntools.urls'))
    3. Add a URL to urlpatterns:  path('dezignprocess/', include
    ('dezignprocess.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("dezigntools.urls"), name="dezigntools_urls"),
    path("", include("dezignprocess.urls"), name="dezignprocess_urls"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include('rest_auth.urls')),
    path("accounts/", include('rest_auth.registration.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    ]
