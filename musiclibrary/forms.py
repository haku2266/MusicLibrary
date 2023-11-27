from django import forms
# from django.forms import HiddenInput, TextInput
from .models import ArtistModel, AlbumModel, SongModel


class ArtistRegisterFrom(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = ['nickname']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'nickname',
                'class': 'form-control'
            })
        }


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['title', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'album title',
                'class': 'form-control'
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }


class AddSongForm(forms.ModelForm):
    class Meta:
        model = SongModel
        exclude = ['uploaded_at']
