from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication, permissions
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
