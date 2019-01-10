"""
This file handles meetup related HTTP requests.
"""

from flask import request
from flask_restplus import Resource

# local import
from api.v1.main.util.meetup_dto import MeetupDto
from api.v1.main.service.meetup_service import save_new_meetup, accessing_meetup

api = MeetupDto.api
meetup = MeetupDto.meetup

@api.route('/create')
class CreateMeetup(Resource):

    @api.response(201, 'Meetup has been created successfully')
    @api.doc('Create a new meetup')
    @api.expect(meetup, validate=True)
    def post(self):
        """
        Create a new meetup.
        """
        data = request.json
        return save_new_meetup(meetup_data=data)

@api.route('/<meetup_id>')
@api.param('meetup_id', 'Meetup Identification.')
@api.response(404, 'Meetup not found in the database')
class SpecificMeetup(Resource):
    @api.doc('Get a specific meetup using the meetup id')
    @api.marshal_list_with(meetup)
    def get(self, meetup_id):
        return accessing_meetup(meetup_id)
        
