from django import forms
# from django.forms import HiddenInput, TextInput

from .models import ConsumerModel


class ConsumerForm(forms.ModelForm):
    class Meta:
        model = ConsumerModel
        fields = ['user', 'is_artist', 'profile_img']
        widgets = {
            'user': forms.TextInput(),
            'is_artist': forms.CheckboxInput(),
            'profile_img': forms.FileInput()
        }


# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.fields['user'].widget = TextInput()
#     self.fields['user'].widget.attrs['disabled'] = 'true'
    # self.fields['user'].widget = HiddenInput()
