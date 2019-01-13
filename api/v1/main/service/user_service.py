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
    password =password=user_data['password']
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
            response_object = {
                'status': 201,
                'message':'You have signed up successfully.'
            }
            return response_object, 201 
        except AssertionError as exc_msg:
            response_object = {
                'status': 400,
            }
            return response_object, 400

    else:
        response_object = {
            'status':409,
            'message':'User with this email address already exist.'
        }
        return response_object, 409
