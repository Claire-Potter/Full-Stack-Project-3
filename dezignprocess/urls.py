from django.urls import path
from dezignprocess import views


urlpatterns = [
    path("first/", views.StepList.as_view(), name="first"),
    path("next/", views.StepNext.as_view(), name="next"),
    path("search/", views.search, name="search"),
    path("<slug:slug>/", views.StepDetail, name="step_detail"),
    path("tools/<slug:slug>/",
         views.ToolsList, name="step_tools"),

]
