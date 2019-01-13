"""This file validates user inputs.
"""

import re
from api.v1.main.model.user import User

class Validator(User):
    def __init__(self, username, email):
        User.__init__(self)

        self.username=username
        self.email = email

    def validate_email(self):
        """
        Validates user email.
        """
        if not self.email:
            raise AssertionError('No email provided')

        if not re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.email):
            raise AssertionError('Check format of your email.')
        return self.email

    def validate_username(self):
        """
        This method validates the usernname.
        """
        if not self.username:
            raise AssertionError('No uaername provided')
        if len(self.username)<4 or len(self.username) >15:
            raise AssertionError('Username must be between 4 and 15 characters')

        return self.username
