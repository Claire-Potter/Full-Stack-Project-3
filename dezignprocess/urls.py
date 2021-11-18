from django.urls import path
from . import views


urlpatterns = [
    path("search/", views.StepSearch, name="search"),
    path("", views.StepList.as_view(), name="home"),
    path("next/", views.StepNext.as_view(), name="next"),
    path("<slug:slug>/", views.StepDetail.as_view(), name="step_detail"),
]
