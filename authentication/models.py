from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from .model_manager import CustomUserManager
from django.conf import settings
import uuid
import datetime
import os


def image_upload_location(instance, file_name:str)->str:
    """Returns image upload location for a user by creating a folder structure
    like /media/username/profile_photos/image.jpeg

    Args:
        instance (CustomUser): An object of CustomUser model
        file_name (str): Name of the image being uploaded.

    Returns:
        str: Folder path where image will be uploaded
    """
    return os.path.join(settings.MEDIA_ROOT, instance.username, 'profile_photos', file_name)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to=image_upload_location, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']


    def __str__(self)->str:
        """Return String representation of CustomUser model

        Returns:
            str: Username and name of CustomUser model
        """
        return f'Username: {self.username}, Name: {self.name}'

