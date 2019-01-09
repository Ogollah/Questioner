"""
This file handles user related HTTP requests
"""

from flask import request
from flask_restplus import Resource

# local import
from api.v1.main.util.user_dto import UserAuthDto
from api.v1.main.service.user_auth_service import UserAuth

api = UserAuthDto.api
user_auth = UserAuthDto.user_auth

@api.route('/signin')
class SigninUser(Resource):
    """
    User login resource
    """
    @api.doc('User signin')
    @api.expect(user_auth, validate=True)
    def post(self):
        user_data = request.json
        return UserAuth.signin_user(data=user_data)
