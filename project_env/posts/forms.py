from django import forms
from .models import Posts, Comments
from ckeditor.widgets import CKEditorWidget


class PostCreate(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Posts
        fields = ['title', 'overview', 'content', 'category', 'thumbnail']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 60
            })
        }