'''
Generic views to provide endpoints for Course, Chapter and Grade APIs
'''
from rest_framework import views, response, status
from django.http import Http404
from course import serializers
from .models import Course, Chapter, Grade


class CourseList(views.APIView):
    """
    List all courses, or create a new course.
    """

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
        serializer = serializers.CourseCreateSerializer(data=request.data)
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
