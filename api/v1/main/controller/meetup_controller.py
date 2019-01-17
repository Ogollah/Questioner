"""
This file handles meetup related HTTP requests.
"""

from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError,InvalidHeaderError,RevokedTokenError
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidAudienceError

# local import
from api.v1.main.util.meetup_dto import MeetupDto
from api.v1.main.service.meetup_service import save_new_meetup, accessing_meetup, get_all_meetups, update_meetup, delete_meetup

api = MeetupDto.api
meetup = MeetupDto.meetup

# create a meetup

@api.route('/create')
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(RevokedTokenError)
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


# accessing all meetups

@api.route('/upcoming') 
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(RevokedTokenError)
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
@api.errorhandler(RevokedTokenError)
@api.errorhandler(InvalidHeaderError)
@api.route('/<int:meetup_id>')
@api.param('meetup_id', 'Meetup Identification.')
@api.response(404, 'Meetup not found in the database')
class SpecificMeetup(Resource):
    @api.doc(security='Bearer Auth')
    @api.doc('Get a specific meetup using the meetup id')
    @api.marshal_list_with(meetup)
    @jwt_required
    def get(self, meetup_id):
        """Get a specific meetup
        """
        return accessing_meetup(meetup_id)

        

@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(RevokedTokenError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
@api.route('/<int:meetup_id>/update')
@api.param('meetup_id', 'Meetup Identification.')
@api.response(404, 'Meetup not found in the database')
class UpdateSpecificMeetup(Resource):
    @api.doc(security='Bearer Auth')
    @api.doc('Update a specific meetup using the meetup id')
    @api.expect(meetup, validate=True)
    @jwt_required
    def patch(self, meetup_id):
        """Get a specific meetup
        """

        input_data = request.json
        return update_meetup(meetup_data=input_data, meetup_id=meetup_id)


@api.route('/<int:meetup_id>/delete')
@api.param('meetup_id', 'Meetup Identification')
@api.errorhandler(NoAuthorizationError)
@api.errorhandler(ExpiredSignatureError)
@api.errorhandler(RevokedTokenError)
@api.errorhandler(InvalidTokenError)
@api.errorhandler(InvalidHeaderError)
class CreateQuestion(Resource):

    @api.response(200, 'Meetup deleted successfully')
    @api.doc('Downvote a Question')
    @api.doc(security='Bearer Auth')
    @jwt_required
    def delete(self,meetup_id):
        """
        Delete a meetup
        """
        return delete_meetup(meetup_id)

