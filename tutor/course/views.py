'''
Generic views to provide endpoints for Course, Chapter and Grade APIs
'''

from rest_framework import views, generics, mixins, response, status
from django.http import Http404
from course.serializers import CourseGetSerializer, CourseCreateSerializer, ChapterCreateSerializer, ChapterGetSerializer, GradeSerializer
from .models import Course, Chapter, Grade


class CourseList(views.APIView):
    """
    List all courses, or create a new course.
    """

    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseGetSerializer(courses, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(views.APIView):
    """
    Retrieve, update or delete a course instance.
    """

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseGetSerializer(course)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseGetSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class ChapterList(views.APIView):
    """
    List all chapters, or create a new chapter.
    """

    def get(self, request, format=None):
        chapters = Chapter.objects.all()
        serializer = ChapterGetSerializer(chapters, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChapterCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapterDetail(views.APIView):
    """
    Retrieve, update or delete a chapter instance.
    """

    def get_object(self, pk):
        try:
            return Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chapter = self.get_object(pk)
        serializer = ChapterGetSerializer(chapter)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        chapter = self.get_object(pk)
        serializer = ChapterGetSerializer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chapter = self.get_object(pk)
        chapter.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class GradeList(views.APIView):
    """
    List all courses, or create a new course.
    """

    def get(self, request, format=None):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GradeDetail(views.APIView):
    """
    Retrieve, update or delete a grade instance.
    """

    def get_object(self, pk):
        try:
            return Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grade = self.get_object(pk)
        serializer = GradeSerializer(grade)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        grade = self.get_object(pk)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grade = self.get_object(pk)
        grade.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
