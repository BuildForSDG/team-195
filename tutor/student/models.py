'''
    A model to create a students' app
    table student to store student's records
'''

from django.db import models


class Students(models.Model):

    '''
        Students' model
    '''

    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    educationlevel = models.CharField(max_length=20)
