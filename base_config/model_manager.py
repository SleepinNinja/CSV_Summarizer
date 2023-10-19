from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from typing import Any

class BaseManager(models.Manager):
    def get_object_or_none(self, **kwargs):
        if not kwargs:
            raise ValueError('Key to find user is required.')
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None 