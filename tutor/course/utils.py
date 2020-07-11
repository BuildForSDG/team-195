"""
    Custom error messages for courses views
"""
from rest_framework.exceptions import APIException
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import exception_handler


class TutorAuthentication(BaseAuthentication):
    """
        It only allows just tutors to perform the specified actions
    """

    message = "You are not allowed to perform this action, just tutors only"

    def has_permission(self, request, view):
        """
            Returns true if is_staff is true
        """

        return request.user.is_staff == True


class CourseNotFound(APIException):

    '''
        This exception provide a good custom error message,
        when a course is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the course dosen\'t exist'
    default_code = "course_not_found"


class GradeNotFound(APIException):

    '''
        This exception provide a good custom error message,
        when a grade level is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the grade class dosen\'t exist'
    default_code = "grade_not_found"


class PostNotFound(APIException):

    '''
        This exception provide a good custom error message,
        when a post is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the post dosen\'t exist'
    default_code = "post_not_found"


class CommentNotFound(APIException):
    
    '''
        This exception provide a good custom error message,
        when a comment is not found.
    '''

    status_code = 404
    default_detail = 'Sorry the comment dosen\'t exist'
    default_code = "comment_not_found"
