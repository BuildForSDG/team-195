'''
Definition of the various endpoints for courses, chapters and grades.
'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from course import views


urlpatterns = [
    # courses
    path('', views.CourseList.as_view()),
    path('<int:pk>/', views.CourseDetail.as_view()),
    # chapters
    path('chapters/', views.ChapterList.as_view()),
    path('chapters/<int:pk>/', views.ChapterDetail.as_view()),
    # grades
    path('grades/', views.GradeList.as_view()),
    path('grades/<int:pk>/', views.GradeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
