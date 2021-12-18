"""
Xperiencedezignwiz dezignprocess app Forms Configuration

The CommentForm was created according to the
Code Institute 'I Think Therefore I Blog' project but fully
customised for purpose.
The CommentForm is created to refer to the Comment model, display
the body field and capture new content.
The ProgressForm is created to refer to the Progress model,
display the progress field and select a progress status.

Forms for the dezignprocess app to be rendered by dezignprocess/views.py
through the step_detail template.
"""
from django import forms
from .models import Progress, Comment


class CommentForm(forms.ModelForm):
    """
     Form set up to enable a signed in user to create
     a comment and save it on the step detail page.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = Comment
        fields = ('body',)


class ProgressForm(forms.ModelForm):
    """
     Form set up to enable a signed in user to create
     a progress status and save it on the step detail page.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = Progress
        fields = ('progress',)
