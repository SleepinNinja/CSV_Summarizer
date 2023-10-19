from django.contrib.auth.backends import BaseBackend
from .models import (
    CustomUser
)


class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user = CustomUser.objects.get_object_or_none(username=username)
        if not user:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, uuid):
        return CustomUser.objects.get_object_or_none(uuid=uuid)

    # todo: need to implement custom authorization too.