from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
User = get_user_model()


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=50, required=True, label='Confirm password',
                                       widget=forms.PasswordInput(attrs={
                                           'placeholder': 'confirm password',
                                           'class': 'form-control confirm-password-input',
                                       }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'profile_img', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control password-input',
                                                   'placeholder': 'password'}),
            'profile_img': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control ',
                                               'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control ',
                                             'placeholder': 'email'})

        }

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Passwords are not the same!')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    password = forms.CharField(max_length=50, required=True, label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
    }))
