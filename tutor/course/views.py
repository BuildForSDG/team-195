'''
Generic views to provide endpoints for Course, Chapter and Grade APIs
'''
from rest_framework import views, response, status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from course import serializers
from .models import Course, Chapter, Grade, Tutors, Students, Posts
from .serializers import PostsSerrializers
from .utils import TutorAuthentication



class CourseList(views.APIView):
    """
    List all courses, or create a new course.
    """
    permission_classes = (IsAuthenticated, TutorAuthentication,)
    def get(self, request):
        '''
        A get method to list all courses
        '''
        courses = Course.objects.all()
        serializer = serializers.CourseGetSerializer(courses, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        '''
        A post method to create a course
        '''
        serializer = serializers.CourseCreateSerializer(
            data=request.data,
            context={
                'request': request
            }
        )
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(views.APIView):
    """
    Retrieve, update or delete a course instance.
    """

    def get_object(self, pk):
        '''
        A get_object method to return a course instance
        '''
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''
        A get method to list all courses
        '''
        course = self.get_object(pk)
        serializer = serializers.CourseGetSerializer(course)
        return response.Response(serializer.data)

    def patch(self, request, pk):
        '''
        A patch method to partially update a course
        '''
        course = self.get_object(pk)
        serializer = serializers.CourseGetSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''
        A delete method to remove an instance from the db
        '''
        course = self.get_object(pk)
        course.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class ChapterList(views.APIView):
    """
    List all chapters, or create a new chapter.
    """

    def get(self, request):
        '''
        A get method to list all chapters
        '''
        chapters = Chapter.objects.all()
        serializer = serializers.ChapterGetSerializer(chapters, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        '''
        A post method to create a chapter
        '''
        serializer = serializers.ChapterCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapterDetail(views.APIView):
    """
    Retrieve, update or delete a chapter instance.
    """

    def get_object(self, pk):
        '''
        A get_object method to return a chapter instance
        '''
        try:
            return Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''
        A get method to list all chapters
        '''
        chapter = self.get_object(pk)
        serializer = serializers.ChapterGetSerializer(chapter)
        return response.Response(serializer.data)

    def patch(self, request, pk):
        '''
        A patch method to partially update a chapter
        '''
        chapter = self.get_object(pk)
        serializer = serializers.ChapterGetSerializer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''
        A delete method to remove an instance from the db
        '''
        chapter = self.get_object(pk)
        chapter.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class GradeList(views.APIView):
    """
    List all courses, or create a new course.
    """

    def get(self, request):
        '''
        A get method to list all grades
        '''
        grades = Grade.objects.all()
        serializer = serializers.GradeSerializer(grades, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        '''
        A post method to create a grade
        '''
        serializer = serializers.GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GradeDetail(views.APIView):
    """
    Retrieve, update or delete a grade instance.
    """

    def get_object(self, pk):
        '''
        A get_object method to return a grade instance
        '''
        try:
            return Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''
        A get method to list all grades
        '''
        grade = self.get_object(pk)
        serializer = serializers.GradeSerializer(grade)
        return response.Response(serializer.data)

    def patch(self, request, pk):
        '''
        A patch method to partially update a grade
        '''
        grade = self.get_object(pk)
        serializer = serializers.GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''
        A delete method to remove an instance from the db
        '''
        grade = self.get_object(pk)
        grade.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class PostsView(views.APIView):
    """
        An API view which makes subscribed users to
        communicate by exchanging texts on the course.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        '''
        A get_object method to return a post instance
        '''
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def post(self, request, course_id):
        """
            This makes subscribed users to write texts
        """
        courses_view = CourseDetail()
        course_instance = courses_view.get_object(course_id)

        student_object = Students.objects.filter(pk=request.user.id)
        tutor_object = Tutors.objects.filter(pk=request.user.id)

        if tutor_object:
            tutor_object = Tutors.objects.get(pk=request.user.id)

            if tutor_object.course_set.filter(id=course_id).exists():

                serializer = PostsSerrializers(
                    data=request.data,
                    context={
                        'request': request, 'course_id': course_instance
                    }
                )

                # Checks if the request data is valid
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return response.Response(serializer.data, status=201)

                # Returns an error if one the request data is invalid
                return response.Response(serializer.errors, status=400)
            else:
                return response.Response(
                    {
                        "error": "Only a tutor who created this course can "
                                 "post"
                    },
                    status=400
                    )
        elif student_object:

            student_object = Students.objects.get(pk=request.user.id)

            if student_object.course_set.filter(id=course_id).exists():

                serializer = PostsSerrializers(
                    data=request.data,
                    context={
                        'request': request, 'course_id': course_instance
                    }
                )

                # Checks if the request data is valid
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return response.Response(serializer.data, status=201)

                # Returns an error if one the request data is invalid
                return response.Response(serializer.errors, status=400)
            else:
                return response.Response(
                    {
                        "error": "Only students subscribed to this course can"
                                 " post."
                    },
                    status=400
                    )
        else:
            return response.Response(
                {
                    "error": "The user should register as a tutor or student"
                             " to post."
                },
                status=400
                )
    def get(self, request, course_id):
        """
            Get all posts in a particular course forum
        """
        posts = Posts.objects.filter(course_id=course_id)

        serializer = PostsSerrializers(posts, many=True)

        return response.Response(serializer.data, status=200)

    def put(self, request, course_id, post_id):
        '''
            A method that updates the posts's object,
            and returns the updated values.
        '''
        courses_view = CourseDetail()
        courses_view.get_object(course_id)

        student_object = Students.objects.filter(pk=request.user.id)
        tutor_object = Tutors.objects.filter(pk=request.user.id)

        post_instance = self.get_object(post_id)

        if tutor_object:
            tutor_object = Tutors.objects.get(pk=request.user.id)

            if tutor_object.course_set.filter(id=course_id).exists():

                if post_instance.user_id.id != request.user.id:
                    return response.Response({
                        "error": "You can not edit other user's posts"
                    })
                serializer = PostsSerrializers(
                    post_instance,
                    data=request.data,
                )
                # Checks if the request data passed is valid
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return response.Response(serializer.data, status=200)

                # Returns an error if one the of the request data value is invlid
                return response.Response(serializer.errors, status=400)
            else:
                return response.Response(
                    {
                        "error": "Sorry a tutor who posted it, can only"
                                 " edit it"
                    },
                    status=400
                    )

        elif student_object:
            student_object = Students.objects.get(pk=request.user.id)

            if student_object.course_set.filter(id=course_id).exists():

                if post_instance.user_id != request.user.id:
                    return response.Response({
                        "error": "You can not edit other student's posts"
                    })

                serializer = PostsSerrializers(
                    post_instance,
                    data=request.data
                )

                # Checks if the request data is valid
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return response.Response(serializer.data, status=201)

                # Returns an error if one the request data is invalid
                return response.Response(serializer.errors, status=400)
            else:
                return response.Response(
                    {
                        "error": "Sorry a student subscribed to this"
                                 " course can edit this post."
                    },
                    status=400
                    )
        else:
            return response.Response(
                {
                    "error": "You should register as a tutor or student"
                             " to edit his/her post."
                },
                status=400
                )
