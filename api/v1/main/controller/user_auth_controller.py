"""
This file handles user related HTTP requests
"""

from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError,InvalidHeaderError
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidAudienceError

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


@api.route('/signout')
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
class SignoutUser(Resource):
    """
    User signout resource
    """
    @api.doc('User signout')
    @api.expect(user_auth)
    @api.doc(security='Bearer Auth')
    @jwt_required
    def post(self):
        return UserAuth.signout_user()
