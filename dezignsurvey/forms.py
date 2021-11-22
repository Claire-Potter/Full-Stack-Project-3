from .models import Survey
from django import forms
from django.forms import ModelForm


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'email', 'gender', 'age_range']

# Creating a form to add an article.
form = SurveyForm()
        