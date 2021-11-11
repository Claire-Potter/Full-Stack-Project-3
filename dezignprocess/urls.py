from django.urls import path
from . import views


urlpatterns = [
    path("", views.StepList.as_view(), name="home"),
]
