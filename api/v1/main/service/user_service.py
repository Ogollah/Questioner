"""
This file contains logic for user model.
"""

import datetime
import re

# local imports
from api.v1.main.model.user import User, USERS
from api.v1.main.util.validator.user_validator import Validator

def get_user_by_email(email):
    """
    Get user by user email 
    """
    for user in USERS:
        if user.email == email:
            return user

# save new user
def save_new_user(user_data):
    # request for user data
    firstname = user_data["firstname"]
    lastname = user_data["lastname"]
    othername = user_data["othername"]
    phoneNumber = user_data["phoneNumber"]
    email = user_data["email"]
    password =user_data['password']
    username = user_data['username']
    user = get_user_by_email(email=email)

    validate = Validator(email=email, username=username)

    if not user:
        try:
            new_user = User()
            new_user.firstname = firstname
            new_user.lastname = lastname
            new_user.othername=othername
            new_user.phoneNumber = phoneNumber
            new_user.email=validate.validate_email()
            new_user.set_password_hash(password)
            new_user.username=validate.validate_username()
            new_user.registered =datetime.datetime.utcnow()
            USERS.append(new_user)
            saved_user={
                'user_id':new_user.user_id,
                'firstname':new_user.firstname,
                'lastname':new_user.lastname,
                'username':new_user.username,
                'phoneNumber':new_user.phoneNumber,
                'email':new_user.email,
                'registeredOn':str(new_user.registered),
                'password':new_user.password
            }
            response_object = {
                'status': 201,
                'data':saved_user,
                'message':'{}, You have signed up successfully.'.format(username)
            }
            return response_object, 201 
        except AssertionError as exc_msg:
            response_object = {
                'status': 400,
                'message': '{}'.format(exc_msg)
            }
            return response_object, 400

    else:
        response_object = {
            'status':409,
            'message':'User with {} email address already exist.'.format(email)
        }
        return response_object, 409
