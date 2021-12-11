from django import forms
from multi_email_field.forms import MultiEmailField


class EmailForm(forms.Form):
    subject = forms.CharField()
    recipients = MultiEmailField()
    message = forms.CharField(widget=forms.Textarea)
