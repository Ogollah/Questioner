"""
This file handles Reservation related HTTP request.
"""
from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError,InvalidHeaderError
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidAudienceError

# local imports
from api.v1.main.service.rsvp_service import save_new_rsvp
from api.v1.main.util.rvsp_dto import RsvpDto

api = RsvpDto.api
rsvp = RsvpDto.rsvp

@api.route('/<int:meetup_id>/rsvp')
@api.param('meetup_id', 'Meetup Identification')
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
class CreateQuestion(Resource):

    @api.response(201, 'You have successfully reserved a meetup')
    @api.doc('Reserve a meetup')
    @api.expect(rsvp, validate=True)
    @api.doc(security='Bearer Auth')
    @jwt_required
    def post(self, meetup_id):
        """
        Reserve a meetup
        """
        input_data = request.json
        return save_new_rsvp(user_input=input_data, meetup_id=meetup_id)
