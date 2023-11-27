from django import forms

# from django.forms import HiddenInput, TextInput
from .models import ArtistModel, SongModel


class ArtistRegisterFrom(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = ['nickname', 'description']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'nickname',
                'class': 'form-control'
            })
        }


class AddSongForm(forms.ModelForm):

    class Meta:
        model = SongModel
        exclude = ['uploaded_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'lyrics': forms.Textarea(attrs={'class': 'form-control', 'style': 'resize: none;'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
            'artists': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
