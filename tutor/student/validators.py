'''
    A class that validates individual values
    passed by the student.
'''

import re


class ValidateStudentData:
    '''
        A class to validate individual values of passed
        by the users. strings, intergers etc
    '''

    @staticmethod
    def check_white_spaces(*studenttuple):
        '''
            Finds white spaces in a value and returns true.
        '''

        for studentvalue in studenttuple:
            pattern = re.compile(r'\s')
            find_white_space = pattern.search(studentvalue)
            if find_white_space:
                return True
        return False

    @staticmethod
    def check_valid_names(*studenttuple):
        '''
            Check if a name starts with an upper case character
            then followed by lower case characters.
            Returns false else true
        '''
        for studentvalue in studenttuple:
            pattern = re.compile(r'[A-Z]{1}[a-z]+')
            valid_name = pattern.fullmatch(studentvalue)
            if not valid_name:
                return True
        return False

    @staticmethod
    def check_empty_values(**studentdict):
        '''
            Checks if each passed data value is empty.
            Returns true if a value is empty, else false.
        '''
        for value in studentdict.values():
            if not value:
                return True
        return False

    @staticmethod
    def check_address_value(address):
        '''
            Checks if the address is a valid address,
            e.g. "london, UnitedKingdom"
        '''
        pattern = re.compile(r'[A-Z][a-z]+[,]\s[A-Z][a-z]+')
        valid_address = pattern.fullmatch(address)
        if not valid_address:
            return True
        return False

    @staticmethod
    def check_student_age(studentage):
        '''
            It checks for the age of to provide
            the age limit of allowed students.
        '''
        pattern = re.compile(r'6|1[0-9]|2[0-9]|3[0-9]|40')
        valid_age = pattern.fullmatch(studentage)
        if not valid_age:
            return True
        return False
