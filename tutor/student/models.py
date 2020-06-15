'''
    A model to create a students' app
    table student to store student's records
'''

from django.db import models
from django.conf import settings
from django.apps import apps

Grade = apps.get_model('course', 'Grade', require_ready=False)


class Students(models.Model):

    '''
        Students' model
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        primary_key=True, unique=True
    )
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    educationlevel = models.ForeignKey(
        Grade, on_delete=models.PROTECT
    )

    @staticmethod
    def query_students_by_parameter(
            age=None, firstname=None, educationlevel=None
    ):

        '''
            A method that searches students by first name,
            level of education and age.
        '''

        # Query all students whose is age greater than the specified
        # age.
        if age:
            age_query_set = Students.objects.filter(
                age__gt=age
            )
            return age_query_set

        # Query all students whose first names starts with the specified
        # firstname variable letters.
        elif firstname:
            firstname_query_set = Students.objects.filter(
                firstname__startswith=firstname
            )
            return firstname_query_set

        # Query all students whose grade level matches exactlty the specified
        # level in the educationlevel variable.
        elif educationlevel:
            educationlevel_query_set = Students.objects.filter(
                educationlevel__exact=educationlevel
            )
            return educationlevel_query_set

        # If all the query variables are not specified, that is they are
        # None the function returns false.
        else:
            return False
