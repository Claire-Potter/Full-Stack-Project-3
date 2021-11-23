from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Survey
from .forms import SurveyForm


def survey_home(request):
    if request.method == "POST":
        survey_form = SurveyForm(request.POST, request.FILES)
        if survey_form.is_valid():
            survey_form.save()
            messages.success(request, ('Your survey was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
        return redirect("survey_home")

    survey_form = SurveyForm()
    surveys = Survey.objects.all()
    return render(request=request,
                  template_name="survey.html",
                  context={'survey_form': survey_form,
                           'surveys': surveys})
