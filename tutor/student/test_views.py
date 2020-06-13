'''
    Testing Student registration
'''

from json import loads
from rest_framework.test import APIClient
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
    educationlevel = 'Degree'

    # Initialises the client object
    c = APIClient()

    @pytest.fixture()
    def student(self):
        '''
            A fixture that gets a student's id,
            It's used in tests to test if a student's
            record was successfully updated.
        '''

        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 28,
                "educationlevel": self.educationlevel
                }
        )

        data = response.content
        data = loads(data)

        # returns the student's id
        return data['id']

    def test_empty_values(self):
        '''
            Tests if some of values passed are empty
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": '',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": self.educationlevel
                },
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["middlename"] == ["Please provide middle name value"]

    def test_valid_names(self):
        '''
            Tests for valid names
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": 'and',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": self.educationlevel
                }
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "The first , middle, last names"
            " and educationlevel should start with"
            " anuppercase followed by"
            " lowercase characters. e.g Andrew"
            ]

    def test_valid_email(self):
        '''
            Tests for a valid email
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": "njayaandrewgmail.com",
                "age": self.age,
                "educationlevel": self.educationlevel
                }
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["email"] == [
            "Please provide a valid email"
            " address. e.g janedoe125@gmail.com"
            ]

    def test_space_characters(self):
        '''
            Tests for a space character
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": 'Odhi  ambo',
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": self.educationlevel
                }
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

    def test_address_value(self):
        '''
            Tests for an adress value
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": 'california',
                "email": self.email,
                "age": self.age,
                "educationlevel": self.educationlevel
                }
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "Please provide a valid address"
            " value.e.g London, Unitedkingdom"
            ]

    def test_age_value(self):
        '''
            Tests for the age value
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 1000,
                "educationlevel": self.educationlevel
                }
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "Sorry the minimum age of a"
            " student allowed is 6 and the maximum 40"
            ]

    def test_student_registration(self):
        '''
            Tests if the user was successfully registered
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 28,
                "educationlevel": self.educationlevel
                }
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
        assert data["educationlevel"] == self.educationlevel

    def test_update_student_record(self, student):
        '''
            Tests if the student record was successfully modified
        '''

        response = self.c.put(
            '/users/students/'+str(student)+'/', {
                "firstname": 'Fodi',
                "middlename": 'Obore',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 20,
                "educationlevel": self.educationlevel
                }
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
        assert data["educationlevel"] == self.educationlevel

    def test_student_record_notfound(self):
        '''
            Tests if the student record dosen't exist
        '''
        response = self.c.put(
            '/users/students/1/', {
                "firstname": 'Fodi',
                "middlename": 'Obore',
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": 20,
                "educationlevel": self.educationlevel
                }
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["detail"] == "Not found."
