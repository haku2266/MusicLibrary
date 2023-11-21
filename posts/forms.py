from django import forms
from .models import CreatePostModel


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePostModel
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title'}),
            'text': forms.Textarea(attrs={'style': 'resize: none;',
                                          'placeholder': 'Post Content'})
        }