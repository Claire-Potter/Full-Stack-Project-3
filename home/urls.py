"""
Xperiencedezignwiz home app URL Configuration

URLs for the home app setup according to home/views.py
home = the homepage
the social media views are setup to authorise login via the
various social media apps.
the google verification view is to verify the domain via google cloud
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views. Contact.as_view(), name='contact'),
    path('google50b8ec44e2d448c8.html/',
         views.verification, name='google_verification'),


]
