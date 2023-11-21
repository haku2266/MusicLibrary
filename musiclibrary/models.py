from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ArtistModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist')
    nickname = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'artist'
        verbose_name_plural = 'artists'


