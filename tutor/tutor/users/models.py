"""
    Tutor and Users model

"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    """
        Users model
    """
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        """
            username's URL
        """
        return reverse("users:detail", kwargs={"username": self.username})


class Tutors(models.Model):

    '''
        Tutors' model
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        primary_key=True,
    )
    firstname = models.CharField(max_length=20)
