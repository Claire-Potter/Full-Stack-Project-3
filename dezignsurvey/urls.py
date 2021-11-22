from django.urls import path
from dezignsurvey import views

urlpatterns = [
    path("survey/", views.survey_home, name="survey"),
]
