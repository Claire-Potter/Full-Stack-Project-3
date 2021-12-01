from .models import Progress, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ('progress',)
