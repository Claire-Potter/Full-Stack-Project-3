from django import forms
from .models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('survey_title', 'survey_image', 'slug',
                  'name', 'email', 'gender', 'age_range',
                  'job_title', 'industry')
