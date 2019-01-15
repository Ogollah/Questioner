"""
This class holds user model to store user details
"""
import re
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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
        self.password =  None
        self.isAdmin = False
        self.registered =  None
        self.user_id = User.class_count
        User.class_count+= 1

    def set_password_hash(self, password):
        """Set password hash."""
        if not password:
            raise AssertionError('Password not provided.')

        if not (any(char.islower() for char in password)):
            raise AssertionError('Password should contain a lower case character.')

        if not (any('[@_!#$%^&*()<>?/\|}{~:]' for char in password)):
            raise AssertionError('Password must contain a special character.')

        if not (any(char.isupper() for char in password)):
            raise AssertionError('Password should contain a capital letter.')

        if not (any(char.isdigit() for char in password)):
            raise AssertionError('Password should contain a number.')

        if len(password)<6 or len(password) > 16:
            raise AssertionError('Password must be between 4 and 16 characters.')
    
        self.password = generate_password_hash(password)

        #compare password with the saved password_hash
    def check_password_hash(self, password):
        """Check password hash."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "'{}'>".format(self.username)

# save admin
user = User()
user.firstname = "kalume"
user.lastname = "Minzi"
user.othername = "Laz"
user.phoneNumber = "+25723456712"
user.email = "admin@admin.com"
user.set_password_hash("#Sadm@3In")
user.username = "useradmin"
user.registered =datetime.datetime.now()
user.isAdmin=True
USERS.append(user)

# save admin 2
user2 = User()
user2.firstname = "Hezzy"
user2.lastname = "Marimu"
user2.othername = "John"
user2.phoneNumber = "+25723456712"
user2.email = "admin2@admin.com"
user2.set_password_hash("@Aadm@3In")
user2.username = "useradmin2"
user2.registered =datetime.datetime.now()
user2.isAdmin=True
USERS.append(user2)

