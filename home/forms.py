from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField()
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
