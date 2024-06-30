from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change the related name here
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change the related name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )





