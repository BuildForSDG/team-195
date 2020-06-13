""""
    View classes to add tutors and users
"""
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from course.utils import TutorAuthentication
from .serializers import TutorsSerializer, UsersSerializer
from .serializers import Tutors



User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class AllUsersView(APIView):
    """
        A view to add a user
    """

    def post(self, request):
        """
            This function creates a user
        """

        serializer = UsersSerializer(data=request.data)
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)


class TutorsView(APIView):
    """
        A view to add a tutor
    """

    permission_classes = (TutorAuthentication,)

    def get_object(self, p_k):
    
        """
            Gets tutor's object, incase it doesn't exists
            it throws an exception the course record wasn't found.
        """

        try:
            return Tutors.objects.get(pk=p_k)
        except Tutors.DoesNotExist:
            raise Http404

    def post(self, request):
        """
            This function creates a tutor
        """

        serializer = TutorsSerializer(data=request.data)
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)

    def get(self, request, p_k):
        """
            Gets a tutor and all the courses he/she created
        """

        tutor = self.get_object(p_k)

        serialized_tutor = TutorsSerializer(tutor)

        return Response(serialized_tutor.data, status=200)
