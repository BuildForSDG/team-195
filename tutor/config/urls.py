"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from student.views import StudentsView, StudentTakeCourseView
from tutor.users.views import AllUsersView, TutorsView, LogoutView, SigninView


urlpatterns = [
    path('api-token-auth/', SigninView.as_view(), name='api_token_auth'),
    path('users/logout/', LogoutView.as_view()),
    path('users/add/', AllUsersView.as_view()),
    path('users/tutors/register/', TutorsView.as_view()),
    path('users/tutors/<int:p_k>', TutorsView.as_view()),
    path('users/students/register', StudentsView.as_view()),
    path('users/students/update', StudentsView.as_view()),
    # path('users/students/<int:p_k>/', StudentsView.as_view()),
    path('users/students/delete/<int:p_k>/', StudentsView.as_view()),
    re_path(r'^users/students/all/(?P<p_k>[0-9]*)$', StudentsView.as_view()),
    path(
        'users/students/<int:student_id>/courses/<int:course_id>/take_course',
        StudentTakeCourseView.as_view()
    ),
    path(
        "", TemplateView.as_view(template_name="pages/home.html"), name="home"
    ),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"),
        name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("courses/", include("course.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] +\
            urlpatterns
