"""
    A class to validate Tutor's and signup field values
"""
import re
from student.serializers import ValidateStudentData


class ValidateTutorFields(ValidateStudentData):
    """
        Uses validators from the parent class it inherits and
        defines validation methods specific to the tutors
    """

    @staticmethod
    def check_tutor_age(tutor_age):
        """
            Checks if the user has the valid age to be a tutor
            in the platform
        """
        pattern = re.compile(r'25|2[5-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|70')
        valid_age = pattern.fullmatch(tutor_age)
        if not valid_age:
            return True
        return False

    @staticmethod
    def check_level_of_education(level):
        """
            Checks if the tutor has provided a valid level of education
        """
        pattern = re.compile(
            r'(College|University|Institute|Law School|Polytechnic)'
        )
        valid_level = pattern.fullmatch(level)
        if not valid_level:
            return True
        return False

    @staticmethod
    def check_years_of_experience(years):
        """
            Checks if the user has provided valid years of experience.
        """
        pattern = re.compile(r'[0-9]|1[0-9]|2[0-9]|30')
        valid_years = pattern.fullmatch(years)
        if not valid_years:
            return True
        return False

    @staticmethod
    def check_empoyed_at(institution):
        """
            Checks if the user has provided valid years of experience.
        """
        pattern = re.compile(r'[A-Z][a-z]+')
        valid_institution = pattern.fullmatch(institution)
        if not valid_institution:
            return True
        return False


class ValidateUsersSignup(ValidateStudentData):
    """
        Validates users signup field values
    """

    @staticmethod
    def check_strong_password(password_value):
        '''
            Makes a user to create a strong password.
        '''
        pattern = re.compile(r'[A-Za-z0-9\W]{8,}')
        valid_name = pattern.match(password_value)
        if not valid_name:
            return True
        return False

    @staticmethod
    def check_white_spaces(*userstuple):
        '''
            Finds white spaces in a value and returns true.
            Overrides the parent class method.
        '''

        for uservalue in userstuple:
            user_string_value = str(uservalue)
            pattern = re.compile(r'\s')
            find_white_space = pattern.search(user_string_value)
            if find_white_space:
                return True
        return False
