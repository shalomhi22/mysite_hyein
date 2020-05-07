from django import forms
from .models import Content, Comment

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['name', 'location']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]