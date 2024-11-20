from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from models_app.models.base.models import BaseModel

from utils.file_uploader import uploaded_file_path


class User(AbstractUser, BaseModel):
    username = models.CharField('username', max_length=128, unique=True)
    bio = models.CharField(max_length=512, blank=True, default='')
    email = models.EmailField('email', blank=True)
    avatar = models.ImageField(upload_to=uploaded_file_path, blank=True, default='defaultuser.png')

    date_joined = None
    first_name = None
    last_name = None

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.email


