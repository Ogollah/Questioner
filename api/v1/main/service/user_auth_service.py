"""
This file helps signin and out user.
"""

from flask import request
from flask_jwt_extended import jwt_required, get_raw_jwt, create_access_token, get_jwt_identity


# local import
from api.v1.main.model.user import User
from api.v1.main.service.user_service import get_user_by_email
from api.v1.main.util.validator.user_validator import Validator
blacklist = set()
class UserAuth:

    @staticmethod
    def signin_user(data):
        password = data['password']
        email = data['email']
        user = get_user_by_email(email=email)

        if email == "":
            response_object = {
                'status': 400,
                'message': 'Provide your email adress to signin.'
            }
            return response_object, 400

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
            # generate access token which will be used for authorization header
            access_token = create_access_token(identity=email)
            response_object = {
                'status': 200,
                'message': 'You have signed in successfully.', 
                'access_token': 'Bearer {}'.format(access_token)
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

        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        response_object = {
            'status': 200,
            'message': 'You have signedout successfully.'
        }
        return response_object, 200

    @staticmethod
    def get_admin():
        current_user = get_jwt_identity()
        user = get_user_by_email(current_user)
        is_admin = user.isAdmin
        return is_admin

    @staticmethod
    def get_user_id():
        current_user = get_jwt_identity()
        user = get_user_by_email(current_user)
        user_id = user.user_id
        return user_id

    

