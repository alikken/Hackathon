# Python
from typing import (
    Optional,
    Iterable
)
import random

# Django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator



# Local
from abstracts.models import AbstractModel
# from abstracts import utils


# class CustomUserManager(BaseUserManager):
#     """ClientManager."""

#     def create_user(
#         self,
#         email: str,
#         password: str
#     ) -> 'CustomUser':
        
#         custom_user: 'CustomUser' = self.model(
#             phone_number=self.phone_number,
#             password=password
#         )
#         custom_user.set_password(password)
#         custom_user.save(using=self._db)
#         return custom_user

#     def create_superuser(
#         self,
#         email: str,
#         password: str
#     ) -> 'CustomUser':

#         custom_user: 'CustomUser' = self.model(
#             email=self.normalize_email(email),
#             password=password
#         )
#         custom_user.is_superuser = True
#         custom_user.is_active = True
#         custom_user.is_staff = True
#         custom_user.set_password(password)
#         custom_user.save(using=self._db)
#         return

#     def create_test_user(self) -> 'CustomUser':

#         custom_user: 'CustomUser' = self.model(
#             email=self.normalize_email('root2@gmail.com'),
#             password='qwerty'
#         )
#         custom_user.set_password('qwerty')
#         custom_user.save(using=self._db)
#         return custom_user


class CustomUser(
    AbstractBaseUser, 
    PermissionsMixin,
    AbstractModel
):
    """My custom user."""

    full_name = models.CharField(
        verbose_name='ФИО',
        max_length=255,
        null=True,
        blank=True
    )
    phone_regex = RegexValidator(
        regex=r'^\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?', 
        message="Phone number must be entered in the format: '+77777777777'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )
    is_superuser = models.BooleanField(
        verbose_name='superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='active',
        default=False
    )
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    # objects = CustomUserManager()

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
    



