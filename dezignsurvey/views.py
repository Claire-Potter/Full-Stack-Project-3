from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Survey
from .forms import SurveyForm


class Survey(View):

    def get(self, request):
        queryset = Survey.objects.all()
        survey = get_object_or_404(queryset)
        survey_form = SurveyForm()

        return render(
            request,
            "survey.html",
            {
                "survey_form": SurveyForm(),
            },
        )

    def post(self, request):
        queryset = Survey.objects.all()
        survey = get_object_or_404(queryset)
        survey_form = SurveyForm(data=request.POST)

        if survey_form.is_valid():

            survey_form.instance.email = request.user.email
            survey_form.instance.username = request.user.username
            survey = survey_form.save(commit=False)
            survey.save()
            messages.success(request, 'Survey completion successful')
        else:
            survey_form = SurveyForm()

        return render(
            request,
            "survey.html",
            {
                "survey_form": SurveyForm(),
            },
        )

