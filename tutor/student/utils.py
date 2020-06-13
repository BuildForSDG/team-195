'''
    These are utility classes to override
    exception messages in the views.
'''

from rest_framework.exceptions import APIException
from rest_framework.authentication import BaseAuthentication


class StudentNotFound(APIException):

    '''
        This exception provide a good custom error message,
        when a student is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the student with the id dosen\'t exist'
    default_code = "student_not_found"


class CourseNotFound(APIException):

    '''
        This exception provide a good custom error message,
        when a course is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the course you are trying to take dosen\'t exist'
    default_code = "course_not_found"


class StudentAuthentication(BaseAuthentication):
    """
        It only allows just students to perform the specified actions
    """

    message = "You are not allowed to perform this action, just students only"

    def has_permission(self, request, view):
        """
            Returns true if is_staff is false
        """

        return request.user.is_staff == False
