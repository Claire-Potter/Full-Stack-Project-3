from django import forms
from multi_email_field.forms import MultiEmailField
from .models import Survey, DefaultQuestion, Question, Option


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
        model = DefaultQuestion
        fields = ['gender', 'age_range', 'industry']
        error_text_inline = False


class BaseAnswerFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs['options'] = kwargs['options'][index]
        return kwargs


class EmailForm(forms.Form):
    subject = forms.CharField()
    recipients = MultiEmailField()
    message = forms.CharField(widget=forms.Textarea)
