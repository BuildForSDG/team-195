'''
    An API view to register a student, update a specific
    student record, delete a specfic student record, view
    a particular student record and getting all students records.
'''

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentsSerializer

# A view to register, delete, view and update students details.


class StudentsView(APIView):

    '''
        Student view class
    '''

    def post(self, request):

        """A method to register a student"""

        serializer = StudentsSerializer(data=request.data)

        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invlid
        return Response(serializer.errors, status=400)
