"""
Xperiencedezignwiz dezigntools app URL Configuration

URLs for the dezigntools app setup according to dezigntools/views.py
URLs configured for the following pages:

Survey-list -summary of user's created surveys
Survey-edit - add questions to a survey
Send-survey-email - send out the survey via email
Survey-detail - view the details of survey submissions
and view answers as percentages
Survey-create - create a new survey
Survey-delete - delete a survey
Survey-question-create - create a new question
Survey-option-create - create options for a question
Survey-start - start answering the survey
Survey-submit - submit option selections
Survey-thanks- thank you for taking the survey
"""
from django.conf import settings
from django.urls import include, path
from dezigntools import views

urlpatterns = [
    path("surveys/", views.survey_list, name="survey-list"),
    path("surveys/<int:p_k>/edit/", views.edit, name="survey-edit"),
    path('surveys/<int:p_k>/email', views.send_email,
         name='send-survey-email'),
    path("surveys/<int:p_k>/", views.detail, name="survey-detail"),
    path("surveys/create/", views.create, name="survey-create"),
    path("surveys/<int:p_k>/delete/", views.delete, name="survey-delete"),
    path("surveys/<int:p_k>/default-options/",
         views.default_options_create,
         name="survey-default-options-create"),

    path("surveys/<int:p_k>/question/", views.question_create,
         name="survey-question-create"),
    path(
        "surveys/<int:survey_pk>/question/<int:question_pk>/option/",
        views.option_create,
        name="survey-option-create",
    ),
    path("surveys/<int:p_k>/start/", views.start, name="survey-start"),
    path("surveys/<int:survey_pk>/submit/<int:sub_pk>/", views.submit,
         name="survey-submit"),
    path("surveys/<int:p_k>/thanks/", views.thanks, name="survey-thanks"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = ([path("__debug__/", include(debug_toolbar.urls)), ] +
                   urlpatterns)
