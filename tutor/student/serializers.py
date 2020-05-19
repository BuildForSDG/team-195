'''
    A model serializer validates data passed by the
    student and changes complex student model data types
    to python simple type that is passed direct to the
    response object in the student view class
'''

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Students
from .validators import ValidateStudentData

# A serializer to get and provide student data


class StudentsSerializer(serializers.ModelSerializer):
    '''
        A Model class to serialize student model
    '''
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
            'id', 'firstname',
            'middlename', 'lastname',
            'Address', 'email',
            'age', 'educationlevel'
        ]
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
                    "required": "Please provide educationlevel key",
                    "blank": "Please provide education level value"
                }
            },
        }

    def validate(self, data):
        '''
            Checks if all values passed by the student are valiid
        '''

        string_values = (
            data['firstname'], data['middlename'],
            data['lastname'], data['educationlevel']
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
                *string_values
            )

        if not_valid_name:
            raise serializers.ValidationError(
                "The first , middle, last names and "
                "educationlevel should start with an"
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

        newstudent = Students.objects.create(**validated_data)
        return newstudent
