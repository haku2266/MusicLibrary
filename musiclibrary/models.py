from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

User = get_user_model()


class ConsumerModel(models.Model):
    def profile_img_dir(user):
        x = f'users/{user}/profile/'
        return x

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    is_artist = models.BooleanField(default=False, null=False, blank=False)
    profile_img = models.ImageField(upload_to=profile_img_dir(user), blank=True, null=True)


@receiver(post_save, sender=User)
def create_consumer(sender, instance, created, **kwargs):
    if created:
        ConsumerModel.objects.create(user=instance)