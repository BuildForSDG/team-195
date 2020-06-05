"""
	This view creates new courses and their chapters
"""
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import viewsets
from course.serializers import CourseSerializer, ChapterSerializer
from .models import Course, Chapter


class IsOwner(BasePermission):

    message = 'You are not allowed to perform this action'

    def has_permission(self, request, view):
        return request.user.is_staff == True


class CourseViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows courses to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'patch','retrieve','delete','head']

    def perform_create(self, serializer):
    	serializer.save()


class ChapterViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows chapters to be viewed or edited.
    """
    
    permission_classes = (IsAuthenticated, IsOwner)

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    http_method_names = ['get', 'post', 'patch','retrieve','delete','head']
