"""
This file handles meetup related HTTP requests.
"""

from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError,InvalidHeaderError
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidAudienceError

# local import
from api.v1.main.util.meetup_dto import MeetupDto
from api.v1.main.service.meetup_service import save_new_meetup, accessing_meetup, get_all_meetups

api = MeetupDto.api
meetup = MeetupDto.meetup

@api.route('/create')
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
class CreateMeetup(Resource):
    @api.response(201, 'Meetup has been created successfully')
    @api.doc('Create a new meetup')
    @api.doc(security='Bearer Auth')
    @api.expect(meetup, validate=True)
    @jwt_required
    def post(self):
        """
        Create a new meetup.
        """
        data = request.json
        return save_new_meetup(meetup_data=data)

@api.route('/upcoming') 
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
@api.doc(security='Bearer Auth')
@api.response(401, 'You need to login first')   
class GetMeetups(Resource):
    @api.doc('List of all available meetups')
    @api.marshal_list_with(meetup)
    @jwt_required
    def get(self):
        """Get a list of all available meetups"""
        return get_all_meetups() 

@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
@api.route('/<int:meetup_id>')
@api.param('meetup_id', 'Meetup Identification.')
@api.response(404, 'Meetup not found in the database')
class SpecificMeetup(Resource):
    @api.doc('Get a specific meetup using the meetup id')
    @api.marshal_list_with(meetup)
    @jwt_required
    def get(self, meetup_id):
        """Get a specific meetup
        """
        return accessing_meetup(meetup_id)
        
