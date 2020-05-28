from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics
from rest_framework import authentication, permissions
from course.serializers import CourseSerializer, ChapterSerializer
from .models import Course, Chapter


class CourseViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows courses to be viewed or edited.
	"""
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	http_method_names = ['get', 'post', 'patch','retrieve','delete','head']

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)

class ChapterViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows chapters to be viewed or edited.
	"""
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer
	http_method_names = ['get', 'post', 'patch','retrieve','delete','head']

class CourseChapterList(generics.ListAPIView):
	serializer_class = ChapterSerializer

	def get_queryset(self):
		"""
		This view should return a list of all the purchases for
		the user as determined by the username portion of the URL.
		"""
		course = self.kwargs['course_id']
		return Chapter.objects.filter(course_id=course)