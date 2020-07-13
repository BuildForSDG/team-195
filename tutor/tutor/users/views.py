""""
    View classes to add tutors and users
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from course.utils import TutorAuthentication
from .serializers import TutorsSerializer, UsersSerializer
from .serializers import Tutors


class AllUsersView(APIView):
    """
        A view to add a user
    """

    def post(self, request):
        """
            This function creates a user
        """

        serializer = UsersSerializer(data=request.data)
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)


class TutorsView(APIView):
    """
        A view to add a tutor
    """

    permission_classes = (TutorAuthentication,)

    def get_object(self, p_k):
        """
            Gets tutor's object, incase it doesn't exists
            it throws an exception the course record wasn't found.
        """

        try:
            return Tutors.objects.get(pk=p_k)
        except Tutors.DoesNotExist:
            raise Http404

    def post(self, request):
        """
            This function creates a tutor
        """

        try:
            Tutors.objects.get(pk=request.user.id)
            return Response({"error": "student registered"})
        except Tutors.DoesNotExist:

            serializer = TutorsSerializer(
                data=request.data,
                context={'request': request}
            )
            # Checks if the request data is valid
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)

            # Returns an error if one the request data is invalid
            return Response(serializer.errors, status=400)

    def get(self, request, p_k):
        """
            Gets a tutor and all the courses he/she created
        """

        tutor = self.get_object(p_k)

        serialized_tutor = TutorsSerializer(tutor)

        return Response(serialized_tutor.data, status=200)


class SigninView(ObtainAuthToken):
    """
        This view log in users
    """

    def post(self, request, *args, **kwargs):
        """
            Logs in users and provides the user's id, username, is_staff
            and  the token as response.
        """
        # Passes request body data and request object too to the serializer
        serializer = self.serializer_class(
            data=request.data,context={'request': request}
        )
        # Raises serializer exceptions in failed login
        serializer.is_valid(raise_exception=True)
        # If the user exists, saves the user object in user variable
        user = serializer.validated_data['user']
        # Generates the token
        token, created = Token.objects.get_or_create(user=user)
        # Provides the response to the user
        return Response(
            {
                'token': token.key, 'user_id': user.pk,
                'username': user.username, 'is_staff': user.is_staff
            },
            status=200
        )


class LogoutView(APIView):
    """
        This view logs users out
    """
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        """
            Gets the authenticated user and
            deletes the token.
        """

        # This deletes the token and forces a login
        request.user.auth_token.delete()
        return Response(
            {'logout_message': 'Succesfully logged out'},
            status=200
        )
