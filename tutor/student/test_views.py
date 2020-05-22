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
    educationlevel = '4th-grade'

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

    @pytest.fixture()
    def save_student(self):
        '''
            A fixture that registers a student,
            and it's used in tests to test if a student's
            record exists.
        '''

        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": self.educationlevel
                }
        )

        data = response.content
        data = loads(data)

        # returns the student's id
        return data

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

    def test_education_level_value(self):
        '''
            Tests if a valid level of education was provided
        '''
        response = self.c.post(
            '/users/students/register', {
                "firstname": self.firstname,
                "middlename": self.middlename,
                "lastname": self.lastname,
                "Address": self.Address,
                "email": self.email,
                "age": self.age,
                "educationlevel": 'Highschool'
                },
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["non_field_errors"] == [
            "Sorry only students in grade school are allowed"
            " to register or provide a valid grade school level"
            " like, 1st-grade, 2nd-grade, 3rd-grade 4, 5..8th-grade"
            ]

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
            " should start with"
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

    def test_student_record_deleted(self, student):
        '''
            Tests if the student record has been successfully
            deleted
        '''
        response = self.c.delete(
            '/users/students/delete/'+str(student)+'/'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data["delete_message"] == "The student record has been deleted"

    def test_delete_student_record_notfound(self):
        '''
            Tests if the student record to be deleted dosen't exist.
        '''
        response = self.c.delete(
            '/users/students/delete/1/'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["detail"] == "Not found."

    def test_get_all_students_records(self, save_student):
        '''
            Tests if all students records are returned.
        '''
        response = self.c.get(
            '/users/students/all/'
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

    def test_get_student_records(self, student):
        '''
            Tests if all students records are returned.
        '''
        response = self.c.get(
            '/users/students/all/'+str(student)
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

    def test_get_student_records_notfound(self):
        '''
            Tests if a student's records fetched wasn't found.
        '''
        response = self.c.get(
            '/users/students/all/2'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["detail"] == "Not found."

    def test_valid_age_query_parameter(self):
        '''
            Tests if age query parameter is a valid integer"
        '''
        response = self.c.get(
            '/users/students/all/?age=six'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["error"] == "Please provide valid age i.e numbers"

    def test_valid_grade_level_query_parameter(self):
        '''
            Tests if grade school level query parameter value
            is a valid level"
        '''
        response = self.c.get(
            '/users/students/all/?educationlevel=grade1'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["error"] ==\
            "Please provide valid grade school level"\
            " e.g 1st-grade, 2nd-grade 3rd..."

    def test_valid_firstname_query_parameter(self):
        '''
            Tests if firstname query parameter value
            is a valid letter"
        '''
        response = self.c.get(
            '/users/students/all/?firstname=234'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 400
        assert data["error"] == "Please provide valid letters"

    def test_empty_firstname_search_results(self):
        '''
            Tests if firstname query search results is
            empty
        '''
        response = self.c.get(
            '/users/students/all/?firstname=A'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 404
        assert data["error"] == 'The search results were not found'

    def test_firstname_search_results(self, save_student):
        '''
            Tests for firstname query search results.
        '''
        response = self.c.get(
            '/users/students/all/?firstname=A'
        )
        data = response.content
        # Changes the response data to a dictionary
        data = loads(data)
        assert response.status_code == 200
        assert data[0]["firstname"] == save_student['firstname']
        assert data[0]["middlename"] == save_student['middlename']
        assert data[0]["lastname"] == save_student['lastname']
