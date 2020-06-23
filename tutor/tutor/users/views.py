""""
    View classes to add tutors and users
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
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
