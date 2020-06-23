"""
    A serializer for  user's and tutor's field values
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from course.serializers import CourseCreateSerializer
from .validators import ValidateTutorFields, ValidateUsersSignup
from .models import Tutors
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    '''
        A Model class to serialize Users model
    '''
    username = serializers.CharField(
        error_messages={
            "required": "Please provide username as key",
            "blank": "Please provide username value."
        },
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user is registered with the same username, please"
                        " choose another username"
            )
        ]
    )
    password = serializers.CharField(
        error_messages={
            "required": "Please provide password as key",
            "blank": "Please provide password value."
        },
        write_only=True
    )
    confirm_password = serializers.CharField(
        error_messages={
            "required": "Please provide confirm_password as key",
            "blank": "Please provide confirm password value."
        },
        write_only=True
    )

    class Meta:
        '''
           The model and fields to be serialized
        '''
        model = User
        fields = [
            'id', 'username',
            'password', 'confirm_password', 'is_staff'
        ]
        extra_kwargs = {
            "is_staff": {
                "error_messages": {
                    "required": "Please provide is_staff as key",
                    "blank": "Please provide is_staff value"
                }
            },
        }
    
    def validate(self, data):
        """
            Validates user signup field values
        """
        # String field values
        string_values = (
            data['username'], data['password'],
            data['is_staff']
        )

        # Checks for space characters
        have_white_space =\
            ValidateUsersSignup.check_white_spaces(
                *string_values
            )

        if have_white_space:
            raise serializers.ValidationError(
                "The username, password, and is staff values shouldn't have"
                " white spaces before, after or within."
            )

        # Checks for a strong password
        not_strong_password =\
            ValidateUsersSignup.check_strong_password(
                data['password']
            )

        if not_strong_password:
            raise serializers.ValidationError(
                "The password should have atleast an uppercase and lowercase,"
                " a digit, special character and have atleast "
                "8 characters too"
            )

        # Checks if the password and confirm password match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                "The password, and confirm password do not match."
            )

        return data    

    def create(self, validated_data):

        '''
            Adds  a new user to the database
        '''

        new_user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=validated_data['is_staff']
        )
        return new_user


class TutorsSerializer(serializers.ModelSerializer):
    '''
        A Model class to serialize Tutors model
    '''
    course_set = CourseCreateSerializer(read_only=True, many=True)

    email = serializers.EmailField(
        error_messages={
            "invalid": "Please provide a valid email address"
                       ". e.g janedoe125@gmail.com"
        },
        validators=[
            UniqueValidator(
                queryset=Tutors.objects.all(),
                message="The email already exists, please provide another"
                        " email"
            )
        ]
    )

    class Meta:
        '''
           The model and fields to be serialized
        '''
        model = Tutors
        fields = (
            'user', 'firstname', 'middlename', 'lastname',
            'age', 'email', 'levelofeducation', 'employed_at',
            'years_of_experience', 'course_set'
        )
        read_only_fields = ('user',)
        extra_kwargs = {
            "firstname": {
                "error_messages": {
                    "required": "Please provide firstname key",
                    "blank": "Please provide first name value"
                }
            },
            "middlename": {
                "error_messages": {
                    "required": "Please provide middlename key",
                    "blank": "Please provide middle name value"
                }
            },
            "lastname": {
                "error_messages": {
                    "required": "Please provide lastname key",
                    "blank": "Please provide last name value"
                }
            },
            "Address": {
                "error_messages": {
                    "required": "Please provide Address key",
                    "blank": "Please provide address value"
                }
            },
            "email": {
                "error_messages": {
                    "required": "Please provide email key",
                    "blank": "Please provide email value",
                }
            },
            "age": {
                "error_messages": {
                    "required": "Please provide age key",
                    "blank": "Please provide age value"
                }
            },
            "levelofeducation": {
                "error_messages": {
                    "required": "Please provide levelofeducation key",
                    "blank": "Please provide levelofeducation value"
                }
            },
            "employed_at": {
                "error_messages": {
                    "required": "Please provide employed_at key",
                    "blank": "Please provide employed_at value"
                }
            },
            "years_of_experience": {
                "error_messages": {
                    "required": "Please provide years_of_experience key",
                    "blank": "Please provide years_of_experience value"
                }
            },
        }

    def validate(self, data):
        '''
            Checks if all ield values passed by the tutor are valiid
        '''
        # String field values
        string_values = (
            data['firstname'], data['middlename'],
            data['lastname']
        )
        # Tutor full name should have valid characters
        valid_string_names = (
            data['firstname'], data['middlename'],
            data['lastname']
        )

        # Checks for space characters
        have_white_space =\
            ValidateTutorFields.check_white_spaces(
                *string_values
            )

        if have_white_space:
            raise serializers.ValidationError(
                "The first, middle, last names shouldn't have"
                " white spaces before, after or within"
            )

        # Checks if full name are valid names
        not_valid_name =\
            ValidateTutorFields.check_valid_names(
                *valid_string_names
            )

        if not_valid_name:
            raise serializers.ValidationError(
                "The first , middle, last names "
                "should start with an"
                "uppercase followed by lowercase characters. e.g Andrew"
            )

        # Checks if it's a valid age for a tutor
        age_string = str(data['age'])
        not_valid_age =\
            ValidateTutorFields.check_tutor_age(
                age_string
            )
        if not_valid_age:
            raise serializers.ValidationError(
                "Sorry the minimum tutor's age allowed is"
                " is 25 and the is maximum 70"
            )

        # Check for a valid education level
        not_valid_level =\
            ValidateTutorFields.check_level_of_education(
                data['levelofeducation']
            )

        if not_valid_level:
            raise serializers.ValidationError(
                "Please provide level of education as 'College', 'University',"
                " 'Law School' or 'Polytechnic', the first letter should be"
                " uppercase."
            )
        # Checks for a valid years of experience
        years_string = str(data['years_of_experience'])
        not_valid_years =\
            ValidateTutorFields.check_years_of_experience(
                years_string
            )
        if not_valid_years:
            raise serializers.ValidationError(
                "Sorry the minimum years of a experience"
                " is 0 and the is maximum 30"
            )

        # Checks for a valid institution name
        not_valid_institution_name =\
            ValidateTutorFields.check_empoyed_at(
                data['employed_at']
            )
        if not_valid_institution_name:
            raise serializers.ValidationError(
                "Please provide valid institution name as one word and"
                " it's first letter should be uppercase"
            )

        return data

    def create(self, validated_data):

        '''
            Adds  a new user to the database
        '''
        user = self.context.get("request").user

        new_user = Tutors.objects.create(user=user, **validated_data)
        return new_user
