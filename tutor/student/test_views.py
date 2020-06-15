'''
    Testing Student registration
'''

from json import loads
from rest_framework.test import APIClient
from django.test import Client
import pytest


@pytest.mark.django_db
class TestStudentRegistration():
    '''
        A class for testing all values
        passed in the student view APIview
    '''

    # Variables, a mock of the values passed to the api view

    firstname = 'Andrew'
    middlename = 'Njaya'
    lastname = 'Odhiambo'
    Address = 'Mombasa, Kenya'
    email = 'njayaandrew@gmail.com'
    age = 28
    educationlevel = '4th-grade'

    # Initialises the client object
    client = Client()
    api_client = APIClient()

    # -------------------------------- fixtures ----------------------------

    @pytest.fixture()
    def user(self):
        '''
            A fixture that gets a user's id,
            this id is then used by another fixture
            to register the user as a student.
        '''

        response = self.client.post(
            '/users/add/', {
                "username": 'WillyMzae',
                "password": "W1984m1$",
                "confirm_password": "W1984m1$",
                "is_staff": 'true'
                }
        )

        data = response.content
        data = loads(data)

        # returns the user's id
        return data['id']

    @pytest.fixture()
    def tutor_token(self, user):
        '''
            This gets the tutor's token
        '''

        response = self.client.post(
            '/api-token-auth/', {
                "username": 'WillyMzae',
                "password": "W1984m1$",
                }
        )

        data = response.content
        data = loads(data)

        # returns the tutor's token
        return data['token']

    @pytest.fixture()
    def tutor(self, tutor_token, user):
        '''
            A fixture that gets a user's id,
            and register him/her as a tutor
        '''

        response = self.client.post(
            '/users/tutors/register/', {

                "firstname": "Willy",
                "middlename": "Mzae",
                "lastname": "Kisao",
                "age": 35,
                "email": "willykisao@gmail.com",
                "levelofeducation": "University",
                "employed_at": "Andela",
                "years_of_experience": 3

            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )

        data = response.content
        data = loads(data)
        print(data)
        # returns the tutor's id
        return data['user']

    @pytest.fixture()
    def grade(self):
        '''
            A fixture that gets a grade's id,
            uses it to add a course
        '''
        response = self.client.post(
            '/courses/grades/', {
                "grade_name": "Five",
            }
        )

        data = response.content
        data = loads(data)
        # returns the grade's id
        return data['id']

    @pytest.fixture()
    def course(self, tutor_token, tutor, grade):
        '''
            A fixture that gets a course's id,
            uses the tutor fixture to add a course
        '''
        response = self.client.post(
            '/courses/', {
                "tutor": tutor,
                "grade": grade,
                "course_name": "Algebra",
                "description": "Introduction to Algebra"
            },
            HTTP_AUTHORIZATION='Token {}'.format(tutor_token)
        )

        data = response.content
        data = loads(data)
        print(data)
        # returns the course's id
        return data['id']

    @pytest.fixture()
    def user_student(self):
        '''
            A fixture that gets a user's id,
            this id is then used by another fixture
            to register the user as a student.
        '''

        response = self.client.post(
            '/users/add/', {
                "username": 'Andrew',
                "password": "A1990n1$",
                "confirm_password": "A1990n1$",
                "is_staff": 'false'
                }
        )

        data = response.content
        data = loads(data)
        # returns the student's id
        return data['id']

    @pytest.fixture()
    def student_token(self):
        '''
            This gets the student's token
        '''

        response = self.client.post(
            '/api-token-auth/', {
                "username": 'Andrew',
                "password": "A1990n1$",
                }
        )

        data = response.content
        data = loads(data)
        print(data)
        # returns the student's token
        return data['token']

    @pytest.fixture()
    def student(self, user_student, grade, student_token):
        '''
            A fixture that gets a student's id,
            It's used in tests to test if a student's
            record was successfully updated.
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 28,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )

        data = response.content
        data = loads(data)

        # returns the student's id
        return data['user']

    @pytest.fixture()
    def save_student(self, user_student, grade, student_token):
        '''
            A fixture that registers a student,
            and it's used in tests to test if a student's
            record exists.
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )

        data = response.content
        data = loads(data)

        # returns the student's id
        return data

    # ------------------------- Testing views ----------------------------

    def test_empty_values(self, user_student, grade, student_token):
        '''
            Tests if some of values passed are empty
        '''

        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": '',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["middlename"] == ["Please provide middle name value"]

    def test_education_level_value(self, user_student, student_token):
        '''
            Tests if a valid level of education was provided
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": 'Highschool'
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["educationlevel"] == [
            "Please provide primary key of the grade name as an integer"
            ]

    def test_valid_names(self, user_student, grade, student_token):
        '''
            Tests for valid names
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": 'and',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "The first , middle, last names"
            " should start with"
            " anuppercase followed by"
            " lowercase characters. e.g Andrew"
            ]

    def test_valid_email(self, user_student, grade, student_token):
        '''
            Tests for a valid email
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": "njayaandrewgmail.com",
                "age": self.age,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["email"] == [
            "Please provide a valid email"
            " address. e.g janedoe125@gmail.com"
            ]

    def test_space_characters(self, user_student, grade, student_token):
        '''
            Tests for a space character
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": 'Odhi  ambo',
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "The first, middle,"
            " last names and address shouldn't"
            " have white spaces before, after or within"
            ]

    def test_address_value(self, user_student, grade, student_token):
        '''
            Tests for an adress value
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": 'california',
                "email": self.email,
                "age": self.age,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "Please provide a valid address"
            " value.e.g London, Unitedkingdom"
            ]

    def test_age_value(self, user_student, grade, student_token):
        '''
            Tests for the age value
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 1000,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "Sorry the minimum age of a"
            " student allowed is 6 and the maximum 40"
            ]

    def test_student_registration(self, user_student, grade, student_token):
        '''
            Tests if the user was successfully registered
        '''
        response = self.client.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 28,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 201
        assert data["firstname"] == self.firstname
        assert data["middlename"] == self.middlename
        assert data["lastname"] == self.lastname
        assert data["Address"] == self.Address
        assert data["email"] == self.email
        assert data["age"] == 28

    def test_update_student_record(self, student, grade, student_token):
        '''
            Tests if the student record was successfully modified
        '''

        response = self.api_client.put(
            '/users/students/update', {
                "firstname": 'Fodi',
                "middlename": 'Obore',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 20,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)

        assert response.status_code == 200
        assert data["firstname"] == 'Fodi'
        assert data["middlename"] == 'Obore'
        assert data["lastname"] == self.lastname
        assert data["Address"] == self.Address
        assert data["email"] == self.email
        assert data["age"] == 20

    def test_student_record_notfound(self, user_student, grade, student_token):
        '''
            Tests if the student record dosen't exist
        '''
        response = self.client.put(
            '/users/students/update', {
                "firstname": 'Fodi',
                "middlename": 'Obore',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 20,
                "educationlevel": grade
            },
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["detail"] == "Sorry the student with the id dosen't exist"

    def test_student_record_deleted(self, student, student_token):
        '''
            Tests if the student record has been successfully
            deleted
        '''
        response = self.client.delete(
            '/users/students/delete/'+str(student)+'/',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data["delete_message"] == "The student record has been deleted"

    def test_delete_student_record_notfound(
        self, user_student, student_token
    ):
        '''
            Tests if the student record to be deleted dosen't exist.
        '''
        response = self.client.delete(
            '/users/students/delete/1/',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["detail"] == "Sorry the student with the id dosen't exist"

    def test_get_all_students_records(
        self, save_student, student_token
    ):
        '''
            Tests if all students records are returned.
        '''
        response = self.client.get(
            '/users/students/all/',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data[0]["firstname"] == save_student['firstname']
        assert data[0]["middlename"] == save_student['middlename']
        assert data[0]["lastname"] == save_student['lastname']
        assert data[0]["Address"] == save_student['Address']
        assert data[0]["email"] == save_student['email']

    def test_get_student_records(self, student, student_token):
        '''
            Tests if all students records are returned.
        '''
        response = self.client.get(
            '/users/students/all/'+str(student),
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data["firstname"] == 'Andrew'
        assert data["middlename"] == 'Njaya'
        assert data["lastname"] == 'Odhiambo'
        assert data["Address"] == 'Mombasa, Kenya'
        assert data["email"] == 'njayaandrew@gmail.com'

    def test_get_student_records_notfound(
            self, user_student, student_token
    ):
        '''
            Tests if a student's records fetched wasn't found.
        '''
        response = self.client.get(
            '/users/students/all/2',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["detail"] == "Sorry the student with the id dosen't exist"

    def test_valid_age_query_parameter(self, user_student, student_token):
        '''
            Tests if age query parameter is a valid integer"
        '''
        response = self.client.get(
            '/users/students/all/?age=six',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["error"] == "Please provide valid age i.e numbers"

    def test_valid_grade_level_query_parameter(
            self, user_student, student_token
    ):
        '''
            Tests if grade school level query parameter value
            is a valid level"
        '''
        response = self.client.get(
            '/users/students/all/?educationlevel=grade1',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["error"] ==\
            "Please provide valid grade school level"\
            " e.g 1st-grade, 2nd-grade 3rd..."

    def test_valid_firstname_query_parameter(
            self, user_student, student_token
    ):
        '''
            Tests if firstname query parameter value
            is a valid letter"
        '''
        response = self.client.get(
            '/users/students/all/?firstname=234',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["error"] == "Please provide valid letters"

    def test_empty_firstname_search_results(self, user_student, student_token):
        '''
            Tests if firstname query search results is
            empty
        '''
        response = self.client.get(
            '/users/students/all/?firstname=A',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["error"] == 'The search results were not found'

    def test_firstname_search_results(self, save_student, student_token):
        '''
            Tests for firstname query search results.
        '''
        response = self.client.get(
            '/users/students/all/?firstname=A',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data[0]["firstname"] == save_student['firstname']
        assert data[0]["middlename"] == save_student['middlename']
        assert data[0]["lastname"] == save_student['lastname']

    def test_student_take_course_course_doesnt_exist(
            self, student, student_token
    ):
        '''
            Tests for firstname query search results.
        '''
        response = self.client.post(
            '/users/students/'+str(student)+'/courses/2/take_course',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data['detail'] == "Sorry the course you are trying "\
            "to take dosen\'t exist"

    def test_student_take_course_student_doesnt_exist(
            self, user_student, course, student_token
    ):
        '''
            Tests for firstname query search results.
        '''
        response = self.client.post(
            '/users/students/1/courses/'+str(course)+'/take_course',
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data['detail'] == "Sorry the student with the id dosen\'t exist"

    def test_student_take_course_successfully(
            self, student, course, student_token
    ):
        '''
            Tests for firstname query search results.
        '''
        response = self.client.post(
            "/users/students/"+str(student)+"/courses/"
            + str(course)+"/take_course",
            HTTP_AUTHORIZATION='Token {}'.format(student_token)
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data['course_set'][0]["course_name"] == "Algebra"
        assert data['course_set'][0]["description"] == "Introduction to "\
            "Algebra"
