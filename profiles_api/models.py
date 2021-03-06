from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from rest_framework.response import Response


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, department, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email adress')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, department=department)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, department, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, department, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'department']

    def get_full_name(self):
        """Retrieve full name os user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email



