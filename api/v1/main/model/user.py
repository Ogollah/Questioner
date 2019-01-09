"""
This class holds user model to store user details
"""

import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# # local imports
# from api.v1.main import bcrypt

USERS = []
class User():
    class_count = 1
    def __init__(self):
        self.email = None
        self.firstname =  None
        self.lastname =  None
        self.othername =  None
        self.phoneNumber =  None
        self.username =  None
        self.password_hash =  None
        self.isAdmin = False
        self.registered =  None
        self.user_id = User.class_count
        User.class_count+= 1

    def set_password_hash(self, password_hash):
        """Set password hash."""
        self.password_hash = generate_password_hash(password_hash)

        #compare password with the saved password_hash
    def check_password_hash(self, password_hash):
        """Check password hash."""
        return check_password_hash(self.password_hash, password_hash)

    def __repr__(self):
        return "User '{}'>".format(self.username)

    # @staticmethod
    # def get_user_by_email(email):
    #     """
    #     Get user by user email 
    #     """
    #     for user in USERS:
    #         if user.email == email:
    #             return user

# save admin
user = User()
user.firstname = "admin"
user.lastname = "admin"
user.othername = "admin"
user.phoneNumber = "+25723456712"
user.email = "admin@admin.com"
user.set_password_hash("admin")
user.username = "admin"
user.registered =datetime.datetime.utcnow() 
user.isAdmin=True
USERS.append(user)

