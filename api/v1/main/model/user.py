"""
This class holds user model to store user details
"""

import datetime

# local imports
from api.v1.main import bcrypt

USERS = []
class User():
    class_count = 1
    def __init__(self, email, firstname, lastname, othername, phoneNumber, username, password_hash, registered, admin=False):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phoneNumber = phoneNumber
        self.username = username
        self.password_hash = password_hash
        self.admin = admin
        self.registered = registered
        self.user_id = User.class_count
        User.class_count += 1

    @property
    def password(self):
        raise AttributeError('Password: Write-only field')

    # set field for the password hasg
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        #compare password with the saved password_hash
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "User '{}'>".format(self.username)
