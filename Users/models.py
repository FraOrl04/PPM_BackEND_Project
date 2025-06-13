from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    "this class is used to create a custom user model"
    bio = models.TextField(blank=True)
    is_moderator = models.BooleanField(default=False)

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
