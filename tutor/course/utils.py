"""
    Custom error messages for courses views
"""

from rest_framework.authentication import BaseAuthentication


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
