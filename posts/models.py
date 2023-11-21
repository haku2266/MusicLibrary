from django.db import models
from musiclibrary.models import ArtistModel


class TagModel(models.Model):
    tag = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class CreatePostModel(models.Model):
    tags = models.ManyToManyField(TagModel, related_name='posts', blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(ArtistModel, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']
