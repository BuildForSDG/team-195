'''
    Validation class for the course models data.
'''

import re


class ValidateCourses:
    '''
        A validation class to validate values passed by users to particular models in course app
    '''

    @staticmethod
    def check_white_spaces(*coursetuple):
        '''
            Finds white spaces in a value and returns true if successful.
        '''

        for coursevalue in coursetuple:
            pattern = re.compile(r'\s')
            find_white_space = pattern.search(coursevalue)
            if find_white_space:
                return True
        return False

    @staticmethod
    def check_valid_names(*coursetuple):
        '''
            Check if a name starts with an upper case
            character followed by lower case characters.
        '''
        for coursevalue in coursetuple:
            pattern = re.compile(r'[A-Z]{1}[a-z]+')
            valid_name = pattern.fullmatch(coursevalue)
            if not valid_name:
                return True
        return False

    @staticmethod
    def check_empty_values(**coursedict):
        '''
            Checks if a passed data value is empty.
            Returns true if successful.
        '''
        for value in coursedict.values():
            if not value:
                return True
        return False
