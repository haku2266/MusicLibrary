from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUserModel(AbstractUser):
    email = models.CharField(blank=False, null=False, unique=True, max_length=100,
                             help_text='Field is unique. '
                                       'You can register with this email only once')
    first_name = models.CharField(blank=False, null=False, max_length=150)
    last_name = models.CharField(blank=False, null=False, max_length=150)
    profile_img = models.ImageField(upload_to='photos/', blank=True, null=True,
                                    help_text='This image will be used as your profile picture')
