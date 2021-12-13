from django import forms
from multi_email_field.forms import MultiEmailField
from .models import Contact


class EmailForm(forms.Form):
    subject = forms.CharField()
    recipients = MultiEmailField()
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    """
     Form set up to enable a user to create
     a contact message and save it on the step detail page.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = Contact
        fields = ('name', 'email', 'body',)
