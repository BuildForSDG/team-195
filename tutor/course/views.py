'''
Model Viewsets to provide endpoints for Course, Chapter and Grade APIs
'''

from rest_framework import viewsets, permissions, authentication
from course.serializers import CourseSerializer, ChapterSerializer, GradeSerializer
from .models import Course, Chapter, Grade


class CourseViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows courses to be viewed or edited.
    '''
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'patch', 'retrieve', 'delete', 'head']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ChapterViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows chapters to be viewed or edited.
    '''
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    http_method_names = ['get', 'post', 'patch', 'retrieve', 'delete', 'head']


class GradeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows school grades to be viewed or edited.
    '''
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    http_method_names = ['get', 'post', 'patch', 'retrieve', 'delete', 'head']
