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


class TagModel(models.Model):
    tag = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class CreatePostModel(models.Model):
    tags = models.ManyToManyField(TagModel, related_name='posts')
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(ArtistModel, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
