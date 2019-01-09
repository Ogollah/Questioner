"""
This file helps signin and out user.
"""

# local import
from api.v1.main.model.user import User
from api.v1.main.service.user_service import get_user_by_email

class UserAuth:

    @staticmethod
    def signin_user(user_data):

        email = user_data['email']
        password = user_data['pasword_hash']
        user = get_user_by_email(email=email)
        user_password = User()
        user_password.check_password_hash(password)

        if user and user_password:
            response_object = {
                'status': 'success',
                'message': 'You have signed in successfully.'
            }
            return response_object, 200

        if user_password and not user:
            response_object = {
                'status': 'fail',
                'message': 'Invalid email, please try again.'
            }
            return response_object, 401

        if user and not user_password:
            response_object = {
                'status': 'fail',
                'message': 'Invalid password, please try again.'
            }
            return response_object, 401

        if not user and not password:
            response_object = {
                'status': 'fail',
                'message': 'User not found, Kindly signup to user this service'
            }
            return response_object, 401
