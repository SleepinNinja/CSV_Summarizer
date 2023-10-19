from django.contrib.auth.models import BaseUserManager
from base_config.model_manager import BaseManager

class CustomUserManager(BaseManager, BaseUserManager):
    def create_user(
            self, 
            username:str=None, 
            password:str=None, 
            **kwargs:dict
        ):
        """Function for creating object of CustomUser as normal user.

        Args:
            username (str, optional): Username for the user. Defaults to None.
            password (str, optional): Password for the user. Defaults to None.

        Raises:
            ValueError: raised if the username is None.

        Returns:
            custom_user: An abject of CustomUser model.
        """
        if not username:
            raise ValueError('Username field is required for creating user.')
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user 

    def create_superuser(
            self, 
            username:str=None, 
            password:str=None, 
            **kwargs:dict
        ):
        """Function for creating object of CustomUser as super user.

        Args:
            username (str, optional): Username for the superuser. Defaults to None.
            password (str, optional): password for the superuser. Defaults to None.

        Raises:
            ValueError: raised if either is_staff or is_superuser is set to False.

        Returns:
            custom_user: An object of customuser as super user.
        """

        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)

        if not all([kwargs.get('is_superuser'), kwargs.get('is_staff')]):
            raise ValueError('Superuser should have is_staff and is_superuser set to True.')

        return self.create_user(username=username, password=password, **kwargs)

