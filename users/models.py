from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    faculty = models.CharField(max_length=255, )
    profile_picture = models.ImageField(upload_to='profile_pictures')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
