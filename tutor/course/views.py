from rest_framework import viewsets
from django.shortcuts import render
from course.serializers import CourseSerializer, ChapterSerializer
from .models import Course, Chapter


class CourseViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows courses to be viewed or edited.
	"""
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows chapters to be viewed or edited.
	"""
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer