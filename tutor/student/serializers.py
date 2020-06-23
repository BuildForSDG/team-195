'''
    A model serializer validates data passed by the
    student and changes complex student model data types
    to python simple type that is passed direct to the
    response object in the student view class
'''

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from course.serializers import CourseCreateSerializer, GradeSerializer
from .models import Students
from .validators import ValidateStudentData

# A serializer to get and provide student data


class StudentsSerializer(serializers.ModelSerializer):
    '''
        A Model class to serialize student model
    '''
    course_set = CourseCreateSerializer(read_only=True, many=True)
    email = serializers.EmailField(
        error_messages={
            "invalid": "Please provide a valid email address"
                       ". e.g janedoe125@gmail.com"
        },
        validators=[
            UniqueValidator(
                queryset=Students.objects.all(),
                message="The email already exists, please provide another"
                        " email"
            )
        ]
    )

    class Meta:
        '''
           The model and fields to be serialized
        '''
        model = Students
        fields = [
            'user', 'firstname', 'middlename', 'lastname',
            'Address', 'email', 'age', 'educationlevel', 'course_set'
        ]
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
            "educationlevel": {
                "error_messages": {
                    'does_not_exist': "The primary key you've provided doesn't"
                                      " exist in grade model",
                    "incorrect_type": "Please provide primary key of the"
                                      " grade name as an integer"
                }
            },
        }

    def validate(self, data):
        '''
            Checks if all values passed by the student are valiid
        '''

        string_values = (
            data['firstname'], data['middlename'],
            data['lastname']
        )

        valid_string_names = (
            data['firstname'], data['middlename'],
            data['lastname']
        )

        valid_string_names = (
            data['firstname'], data['middlename'],
            data['lastname']
        )

        # Checks for space characters
        have_white_space =\
            ValidateStudentData.check_white_spaces(
                *string_values
            )

        if have_white_space:
            raise serializers.ValidationError(
                "The first, middle, last names and address shouldn't have"
                " white spaces before, after or within"
            )

        # Checks for valid names
        not_valid_name =\
            ValidateStudentData.check_valid_names(
                *valid_string_names
            )

        if not_valid_name:
            raise serializers.ValidationError(
                "The first , middle, last names "
                "should start with an"
                "uppercase followed by lowercase characters. e.g Andrew"
            )

        # Checks it's a valid address
        not_valid_address =\
            ValidateStudentData.check_address_value(
                data['Address']
            )
        if not_valid_address:
            raise serializers.ValidationError(
                "Please provide a valid address value."
                "e.g London, Unitedkingdom"
            )

        # Check for a valid age
        age_string = str(data['age'])
        not_valid_age =\
            ValidateStudentData.check_student_age(
                age_string
            )
        if not_valid_age:
            raise serializers.ValidationError(
                "Sorry the minimum age of a student allowed"
                " is 6 and the maximum 40"
            )

        return data

    def create(self, validated_data):

        '''
            Adds  a new student to the database
        '''
        # Gets the authenticated user instance from the request object
        user = self.context.get("request").user

        newstudent = Students.objects.create(
            user=user, **validated_data
        )

        return newstudent

    def update(self, instance, validated_data):

        '''
            Overrides update method of the model serializer
            to updates a student's record.
        '''
        # Updates instance's fields
        instance.firstname = validated_data.get(
            'firstname'
        )
        instance.middlename = validated_data.get(
            'middlename'
        )
        instance.lastname = validated_data.get(
            'lastname'
        )
        instance.Address = validated_data.get('Address')
        instance.email = validated_data.get('email')
        instance.age = validated_data.get('age')
        instance.educationlevel = validated_data.get(
            'educationlevel'
        )
        # returns updated student's instance
        instance.save()
        return instance
