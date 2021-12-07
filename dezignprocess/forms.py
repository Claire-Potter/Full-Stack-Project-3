from django import forms
from .models import Progress, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ('progress',)
