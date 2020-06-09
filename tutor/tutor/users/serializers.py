"""
    A serializer to  user's and tutor's data
"""
from rest_framework import serializers
from .models import Tutors
from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    '''
        A Model class to serialize Users model
    '''

    class Meta:
        '''
           The model and fields to be serialized
        '''
        model = User
        fields = [
            'id', 'username',
            'password', 'email',
            'first_name', 'last_name', 'is_staff'
        ]

    def create(self, validated_data):

        '''
            Adds  a new user to the database
        '''

        new_user = User.objects.create_user(**validated_data)
        return new_user


class TutorsSerializer(serializers.ModelSerializer):
    '''
        A Model class to serialize Tutors model
    '''

    class Meta:
        '''
           The model and fields to be serialized
        '''
        model = Tutors
        fields = [
            'user', 'firstname'
        ]

    def create(self, validated_data):

        '''
            Adds  a new user to the database
        '''

        new_user = Tutors.objects.create(**validated_data)
        return new_user
