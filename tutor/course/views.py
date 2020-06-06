"""
	This view creates new courses and their chapters
"""
from rest_framework import viewsets
from course.serializers import CourseSerializer, ChapterSerializer
from .models import Course, Chapter
from .utils import TutorAuthentication


class CourseViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows courses to be viewed or edited.
    """
    permission_classes = (TutorAuthentication,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'patch','retrieve','delete','head']

    def perform_create(self, serializer):
    	serializer.save()


class ChapterViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows chapters to be viewed or edited.
    """
    
    # permission_classes = (TutorAuthentication)

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    http_method_names = ['get', 'post', 'patch','retrieve','delete','head']
