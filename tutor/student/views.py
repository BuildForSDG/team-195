'''
    An API view to register a student, update a specific
    student record, delete a specfic student record, view
    a particular student record and getting all students records.
'''

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentsSerializer
from .models import Students

# A view to register, delete, view and update students details.


class StudentsView(APIView):

    '''
        Student view class
    '''

    def get_object(self, p_k):

        '''
            Gets student's object, incase it doesn't exists
            it throws an exception the student record wasn't found.
        '''

        try:
            return Students.objects.get(pk=p_k)
        except Students.DoesNotExist:
            raise Http404(
                'Sorry the student with the id dosen\'t  dosen\'t exist'
            )

    def post(self, request):

        """A method to register a student"""

        serializer = StudentsSerializer(data=request.data)

        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invlid
        return Response(serializer.errors, status=400)

    def put(self, request, p_k):

        '''
            A method that updates the student's object,
            and returns the updated values.
        '''

        student = self.get_object(p_k)

        serializer = StudentsSerializer(student, data=request.data)

        # Checks if the request data passed is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

        # Returns an error if one the of the request data value is invlid
        return Response(serializer.errors, status=400)

    def delete(self, request, p_k):

        '''
            Deletes a student's record else it
            raises an exception, the student record wasn't
            found.
        '''

        student_inastance = self.get_object(p_k)

        student_inastance.delete()

        return Response(
            {"delete_message": "The student record has been deleted"},
            status=200
        )
