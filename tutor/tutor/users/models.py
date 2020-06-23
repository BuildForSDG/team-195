"""
    Tutor and Users model

"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):

    """
        Users model
    """

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Tutors(models.Model):

    '''
        Tutors' model
    '''

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        primary_key=True,
    )
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    levelofeducation = models.CharField(max_length=20)
    employed_at = models.CharField(max_length=30)
    years_of_experience = models.IntegerField()
