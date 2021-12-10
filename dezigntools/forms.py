from django import forms
from .models import Survey, DefaultQuestions, Question, Option


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'survey_image']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option']


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options')
        # Options must be a list of Option objects
        choices = {(o.pk, o.option) for o in options}
        super().__init__(*args, **kwargs)
        option_field = forms.ChoiceField(
                                         choices=choices,
                                         widget=forms.RadioSelect,
                                         required=True)
        self.fields['option'] = option_field


class DefaultQuestionsAnswerForm(forms.ModelForm):
    class Meta:
        model = DefaultQuestions
        fields = ['name', 'gender', 'age_range', 'job_title', 'industry']


class BaseAnswerFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs['options'] = kwargs['options'][index]
        return kwargs
