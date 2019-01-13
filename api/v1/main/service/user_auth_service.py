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
        password = data['password']
        user = get_user_by_email(email=data['email'])

        if password == "":
            response_object = {
                'status': 400,
                'message': 'password needed.'
            }
            return response_object, 400

        if not user:
            response_object = {
                'status': 404,
                'message': 'User not found, Kindly signup to user this service'
            }
            return response_object, 404

        if user and user.check_password_hash(password):
            SIGNIN_USERS.append(user)
            response_object = {
                'status': 200,
                'message': 'You have signed in successfully.'
            }
            return response_object, 200

        else:
            #  user_password and not user:
            response_object = {
                'status': 401,
                'message': 'Wrong email or password, please try again.'
            }
            return response_object, 401

    @staticmethod
    def signout_user():
        user = [x for x in SIGNIN_USERS]
        if user:
            SIGNIN_USERS.pop()
            response_object = {
                'status': 200,
                'message': 'You have signedout successfully.'
            }
            return response_object, 200
        else:
            response_object = {
                'status': 401,
                'message': 'You are not logged in'
            }
            return response_object, 401

