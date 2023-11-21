from django import forms
# from django.forms import HiddenInput, TextInput
from .models import ArtistModel


class ArtistRegisterFrom(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = ['nickname']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'nickname'
            })
        }
