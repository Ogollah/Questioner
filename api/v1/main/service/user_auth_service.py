"""
This file helps signin and out user.
"""

from flask import request

# local import
from api.v1.main.model.user import User
from api.v1.main.service.user_service import get_user_by_email

SIGNIN_USERS=[]

class UserAuth:

    @staticmethod
    def signin_user(data):
        password_hash = data['password_hash']
        email = data['email']
        user = get_user_by_email(email=email)

        if password_hash == "":
            response_object = {
                'status': 'fail',
                'message': 'password needed.'
            }
            return response_object, 400

        if not user:
            response_object = {
                'status': 'fail',
                'message': 'User not found, Kindly signup to user this service'
            }
            return response_object, 404

        if user and user.check_password_hash(password_hash):
            SIGNIN_USERS.append(user)
            response_object = {
                'status': 'success',
                'message': 'You have signed in successfully.'
            }
            return response_object, 200

        else:
            #  user_password and not user:
            response_object = {
                'status': 'fail',
                'message': 'Wrong email or password, please try again.'
            }
            return response_object, 401

