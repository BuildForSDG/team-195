'''
    These are utility classes to override
    exception messages in the views.
'''

from rest_framework.exceptions import APIException


class StudentNotFound(APIException):

    '''
        This exception provide a good custom error message,
        when a student is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the student with the id dosen\'t exist'
    default_code = "student_not_found"
