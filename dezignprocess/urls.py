from django.urls import path
from . import views


urlpatterns = [
    path("", views.StepList.as_view(), name="home"),
    path("next/", views.StepNext.as_view(), name="next"),
]
