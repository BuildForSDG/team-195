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
    # Posts
    path(
        'course_forum/course/<int:course_id>/post/',
        views.PostsView.as_view()
    ),
    # View all posts url
    path(
        'course_forum/course/<int:course_id>/posts/',
        views.PostsView.as_view()
    ),
    # Edit a post url
    path(
        'course_forum/course/<int:course_id>/post/<int:post_id>/edit/',
        views.PostsView.as_view()
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
