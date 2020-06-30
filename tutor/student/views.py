'''
    An API view to register a student, update a specific
    student record, delete a specfic student record, view
    a particular student record and getting all students records.
'''

# from django.http import Http404
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from course.serializers import Course
from .serializers import StudentsSerializer, ValidateStudentData
from .models import Students
from .utils import StudentNotFound, CourseNotFound, StudentAuthentication


# A view to register, delete, view and update students details.


class StudentsView(APIView):

    '''
        Student view class
    '''
    permission_classes = (IsAuthenticated, StudentAuthentication,)

    def get_object(self, p_k):

        '''
            Gets student's object, incase it doesn't exists
            it throws an exception the student record wasn't found.
        '''

        try:
            return Students.objects.get(pk=p_k)
        except Students.DoesNotExist:
            raise StudentNotFound

    def post(self, request):

        """A method to register a student"""

        try:
            Students.objects.get(pk=request.user.id)
            return Response(
                {"error": " The user is already registered as a student"}, 
                status=200
            )
        except Students.DoesNotExist:

            serializer = StudentsSerializer(
                data=request.data,
                context={'request': request}
            )

            # Checks if the request data is valid
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)

            # Returns an error if one the request data is invlid
            return Response(serializer.errors, status=400)

    def put(self, request):

        '''
            A method that updates the student's object,
            and returns the updated values.
        '''

        student = self.get_object(request.user.id)

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

    def get(self, request, p_k):

        '''
            Gets all students registered on the platform
        '''

        # Creates a varaiable that holds student's query set
        students_query_set = Students.query_students_by_parameter()

        # Gets query parameters dictionary
        parameters_dict = request.query_params

        # Checks if firstname, age and educationlevel keys
        # exists in the parameters dictionary
        if 'firstname' in parameters_dict:

            firstname = parameters_dict['firstname']

            not_valid_letters = ValidateStudentData.check_string_value(
                firstname
            )
            if not_valid_letters:

                return Response(
                    {"error": 'Please provide valid letters'},
                    status=400
                )

            students_query_set = Students.query_students_by_parameter(
                firstname=firstname
            )

        elif 'age' in parameters_dict:

            age = parameters_dict['age']

            not_valid_interger = ValidateStudentData.check_interger_value(
                age
            )

            if not_valid_interger:

                return Response(
                    {"error": 'Please provide valid age i.e numbers'},
                    status=400
                )

            students_query_set = Students.query_students_by_parameter(
                age=age
            )
        elif 'educationlevel' in parameters_dict:

            gradelevel = parameters_dict['educationlevel']

            not_valid_level = ValidateStudentData.check_education_level(
                gradelevel
            )

            if not_valid_level:

                return Response(
                    {
                        "error": 'Please provide valid grade school level e.g'
                                 ' 1st-grade, 2nd-grade 3rd...'
                    },
                    status=400
                )
            students_query_set = Students.query_students_by_parameter(
                educationlevel=gradelevel
            )
        else:
            pass

        # If the student's query set variable is not an instance
        # of the query set, run the default request
        if not isinstance(students_query_set, QuerySet):
            # If a student id(p_k) is provided, it gets the student's
            # instance
            if p_k:

                # Gets student's object
                student = self.get_object(p_k)

                # Converts the student's object to a python dictionary
                serialized_student = StudentsSerializer(student)

                return Response(serialized_student.data, status=200)

            # Returns a queryset of students order by first name
            all_students = Students.objects.all().order_by('firstname')

            # Returns a list of dictionaries, each dictionary representing
            # a student's record
            all_students_serialized = StudentsSerializer(
                all_students, many=True
                )

            # Returns a json representation of the list of students
            return Response(all_students_serialized.data, status=200)

        else:
            # if the student's query set is an instance of the queryset,
            # this serailizes the query set.
            serialized_queried_students = StudentsSerializer(
                students_query_set, many=True
            )
            # When the serialized query set if empty, it returns 404
            # response.
            if not serialized_queried_students.data:
                return Response(
                    {"error": 'The search results were not found'},
                    status=404
                )
            # Returns the serach results.
            return Response(serialized_queried_students.data, status=200)


# A view where a student can take a course


class StudentTakeCourseView(APIView):
    """
        A view where a student can subscribe and
        unsubscribe to a course, view all courses he/she
        has subcribed to.
    """

    permission_classes = (IsAuthenticated, StudentAuthentication,)

    def get_object(self, p_k):

        """
            Gets course's object, incase it doesn't exists
            it throws an exception the course record wasn't found.
        """

        try:
            return Course.objects.get(pk=p_k)
        except Course.DoesNotExist:
            raise CourseNotFound

    def post(self, request, student_id, course_id):
        """
            A view function to make a student,
            take a course.
        """

        # Instantiates a student's view class
        student_view = StudentsView()

        # Gets the student's instance
        student_instance = student_view.get_object(student_id)

        # Get's a course instance
        course_instance = self.get_object(course_id)

        # Adds a course instance to the student's instance
        student_instance.course_set.add(course_instance)

        # Serializes the student's instance
        serialized_student = StudentsSerializer(
            student_instance
        )

        # Returns a response that add's the course
        # to the list of courses the student is already
        # subscribed to.
        return Response(serialized_student.data, status=200)
