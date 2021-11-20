from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("search/", views.search, name="search"),
    path("first/", views.StepList.as_view(), name="first"),
    path("next/", views.StepNext.as_view(), name="next"),
    path("<slug:slug>/", views.StepDetail.as_view(), name="step_detail"),
]
