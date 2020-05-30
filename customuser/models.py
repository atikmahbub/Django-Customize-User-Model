from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)
from .UserManager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Full_Name = models.CharField(max_length = 100,blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Full_Name'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        if self.Full_Name:
            return self.Full_Name

        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active