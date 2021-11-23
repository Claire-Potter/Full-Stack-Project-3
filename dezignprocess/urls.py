from django.urls import path
from dezignprocess import views


urlpatterns = [
    path("first/", views.StepList.as_view(), name="first"),
    path("next/", views.StepNext.as_view(), name="next"),
    path("search/", views.search, name="search"),
    path("<slug:slug>/", views.StepDetail.as_view(), name="step_detail"),
    path("templates/<slug:slug>/",
         views.TemplatesList.as_view(), name="step_templates"),

]
