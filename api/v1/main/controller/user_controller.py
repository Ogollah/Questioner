"""
This file handles user related HTTP requests
"""

from flask import request
from flask_restplus import Resource

# local import
from api.v1.main.util.user_dto import UserDto,UserAuthDto
from api.v1.main.service.user_service import save_new_user
from api.v1.main.service.user_auth_service import UserAuth

api = UserDto.api
_user = UserDto.user
user_auth = UserAuthDto.user_auth


@api.route('/signup')
class SignupUser(Resource):

    @api.response(201, 'You have signed up successfully.')
    @api.doc('Signup a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """
        Sign up a new user.
        """
        user_data = request.json
        return save_new_user(user_data=user_data)

@api.route('/signin')
class SigninUser(Resource):
    """
    User login resource
    """
    @api.doc('User signin')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_user_data = request.json
        return UserAuth.signin_user(user_data=post_user_data)
        