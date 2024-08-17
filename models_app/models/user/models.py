from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_social_auth = models.BooleanField(default=False)

    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
