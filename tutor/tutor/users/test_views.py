'''
    Testing users and tutors registration
'''

from json import loads
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestUsersRegistration():
    '''
        A class testing all values
        passed in the users' view APIview
    '''

    # Variables, a mock of the values passed to the api view

    username = 'Andrew'
    password = 'A1990n1$'
    confirm_password = 'A1990n1$'
    is_staff = 'true'

    # Initialises the client object
    client = APIClient()

    def test_username_field_empty(self):
        '''
            Tests if the username field value is empty
        '''

        response = self.client.post(
            '/users/add/', {
                "username": '',
                "password": self.password,
                "confirm_password": self.confirm_password,
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["username"][0] == "Please provide username value."

    def test_password_field_empty(self):
        '''
            Tests if the password field value is empty
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.username,
                "password": '',
                "confirm_password": self.confirm_password,
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["password"][0] == "Please provide password value."

    def test_confirm_password_field_empty(self):
        '''
            Tests if the confirm password field value is empty
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.username,
                "password": self.password,
                "confirm_password": '',
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["confirm_password"][0] ==\
            "Please provide confirm password value."

    def test_is_staff_field_empty(self):
        '''
            Tests if the is staff field value is empty
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.username,
                "password": self.password,
                "confirm_password": self.confirm_password,
                "is_staff": ''
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["is_staff"][0] == "Must be a valid boolean."

    def test_password_do_not_match(self):
        '''
            Tests if the password and confirm password fileds,
            don't match.
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.username,
                "password": self.password,
                "confirm_password": 'Andrew',
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "The password, and confirm password do not match."

    def test_strong_password(self):
        '''
            Tests if the password value meets all required characters
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.username,
                "password": 'A1990n',
                "confirm_password": 'A1990n',
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "The password should have atleast an uppercase and lowercase, "\
            "a digit, special character and have atleast 8 characters too"

    def test_space_characters(self):
        '''
            Tests if field values have space characters
        '''

        response = self.client.post(
            '/users/add/', {
                "username": 'And  rew',
                "password": self.password,
                "confirm_password": self.confirm_password,
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "The username, password, and is "\
            "staff values shouldn't have white spaces before, "\
            "after or within."

    def test_user_successfully_registration(self):
        '''
            Tests if field values have space characters
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.username,
                "password": self.password,
                "confirm_password": self.confirm_password,
                "is_staff": self.is_staff
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 201
        assert data["username"] == self.username
        assert data["is_staff"] == True


# This class tests if the tutor has succesfully registered


@pytest.mark.django_db
class TestTutorRegistration():
    '''
        A class for testing all values
        passed in the tutor's APIview
    '''

    # Variables, a mock of the values passed to the view

    firstname = 'Andrew'
    middlename = 'Njaya'
    lastname = 'Odhiambo'
    age = 28
    email = 'njayaandrew@gmail.com'
    levelofeducation = 'University'
    employed_at = 'Andela'
    years_of_experience = 2

    # Initialises the client object
    client = APIClient()

    # -------------------------------- fixtures ----------------------------

    @pytest.fixture()
    def tutor_user(self):
        '''
            A fixture that gets a user's id,
            this id is then used by another fixture
            to register the user as a student.
        '''

        response = self.client.post(
            '/users/add/', {
                "username": self.firstname,
                "password": "A1990n1$",
                "confirm_password": "A1990n1$",
                "is_staff": 'true'
                }
        )

        data = response.content
        data = loads(data)

        # returns a user's id
        return data['id']

    @pytest.fixture()
    def tutor_token(self, tutor_user):
        '''
            This gets the tutor's token
        '''

        response = self.client.post(
            '/api-token-auth/', {
                "username": self.firstname,
                "password": "A1990n1$",
                }
        )

        data = response.content
        data = loads(data)

        # returns the tutor's token
        return data['token']

    def test_firstname_empty_value(self, tutor_user, tutor_token):
        '''
            Tests if some of values passed are empty
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": '',
                "middlename": self.middlename,
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["firstname"][0] == "Please provide first name value"

    def test_middlename_empty_value(self, tutor_user, tutor_token):
        '''
            Tests if middle name value passed is empty
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": '',
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["middlename"][0] == "Please provide middle name value"

    def test_whitespaces_in_value(self, tutor_user, tutor_token):
        '''
            Tests if middlename value has white spaces
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": 'Nja   ya',
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "The first, middle, last names shouldn't"\
            " have white spaces before, after or within"

    def test_valid_name_value(self, tutor_user, tutor_token):
        '''
            Tests if middlename value has valid name
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": 'njaya',
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "The first , middle, last names should start "\
            "with anuppercase followed by lowercase characters"\
            ". e.g Andrew"

    def test_tutor_age_value(self, tutor_user, tutor_token):
        '''
            Tests if user has the required age to be a tutor
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "age": 20,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "Sorry the minimum tutor's age allowed "\
            "is is 25 and the is maximum 70"

    def test_level_of_value(self, tutor_user, tutor_token):
        '''
            Tests if user has the required age to be a tutor
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": 'Highschool',
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "Please provide level of education as 'College', "\
            "'University', 'Law School' or 'Polytechnic', the first "\
            "letter should be uppercase."

    def test_years_of_experience_value(self, tutor_user, tutor_token):
        '''
            Tests if tutor provides valid years of experience
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": 100000
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "Sorry the minimum years of a experience"\
            " is 0 and the is maximum 30"

    def test_employed_at_value(self, tutor_user, tutor_token):
        '''
            Tests if tutor has provide a valid institution
            he or she is currently employed at
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": 'andela',
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"][0] ==\
            "Please provide valid institution "\
            "name as one word and it's first letter should be uppercase"

    def test_successfull_tutor_registration(self, tutor_user, tutor_token):
        '''
            Tests if tutor has been registered successfully
        '''

        response = self.client.post(
            '/users/tutors/register/', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "age": self.age,
                "email": self.email,
                "levelofeducation": self.levelofeducation,
                "employed_at": self.employed_at,
                "years_of_experience": self.years_of_experience
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 201
        assert data["firstname"] == self.firstname
        assert data["middlename"] == self.middlename
        assert data["lastname"] == self.lastname
        assert data["age"] == self.age
        assert data["email"] == self.email
