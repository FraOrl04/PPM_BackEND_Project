from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return self.username