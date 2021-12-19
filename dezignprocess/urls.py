"""
Xperiencedezignwiz dezignprocess app URL Configuration

URLs for the dezignprocess app setup according to dezignprocess/views.py
URLs configured for the following pages:

First - the first list of steps
Next - the second list of steps
Search - the search results when a user searches for a step
Step_Detail - the step detail page accessed from the step
Step_Tools - the step tool page accessed from step_detail

"""
from django.urls import path
from dezignprocess import views


urlpatterns = [

    path('first/', views.StepList.as_view(), name='first'),
    path('next/', views.StepNext.as_view(), name='next'),
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.StepDetail.as_view(), name='step_detail'),
    path('tools/<slug:slug>/',
         views.ToolsList.as_view(), name='step_tools'),


]
