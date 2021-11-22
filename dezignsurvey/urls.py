from django.urls import path
from dezignsurvey import views

urlpatterns = [
    path("survey/", views.Survey.as_view(), name="survey"),
]
