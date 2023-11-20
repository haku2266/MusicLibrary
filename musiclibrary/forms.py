from django import forms
# from django.forms import HiddenInput, TextInput
from .models import ArtistModel, CreatePostModel


class ArtistRegisterFrom(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = ['nickname']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'nickname'
            })
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePostModel
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title'}),
            'text': forms.Textarea(attrs={'style': 'resize: none;',
                                          'placeholder': 'Post Content'})
        }