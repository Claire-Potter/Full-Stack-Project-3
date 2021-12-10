"""
Xperiencedezignwiz dezignprocess app Forms Configuration

Forms for the dezignprocess app to be rendered by dezignprocess/views.py
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
