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
        return "'{}'>".format(self.username)

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
user.firstname = "kalume"
user.lastname = "Minzi"
user.othername = "Laz"
user.phoneNumber = "+25723456712"
user.email = "admin@admin.com"
user.set_password_hash("adm@3In")
user.username = "useradmin"
user.registered =datetime.datetime.utcnow() 
user.isAdmin=True
USERS.append(user)

# save admin 2
user2 = User()
user2.firstname = "Hezzy"
user2.lastname = "Marimu"
user2.othername = "John"
user2.phoneNumber = "+25723456712"
user2.email = "admin2@admin.com"
user2.set_password_hash("adm@3In")
user2.username = "useradmin2"
user2.registered =datetime.datetime.utcnow() 
user2.isAdmin=True
USERS.append(user2)

