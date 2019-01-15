"""
This file marshall meetup data for api call.
"""

from flask_restplus import Namespace, fields

class MeetupDto:
    """
    Meetup details.
    """

    api = Namespace('Meetup Crude Operation', description='Meetup operations')
    meetup = api.model('meetup',{
        'meetup_id': fields.Integer(description='Meetup Identification'),
        'topic': fields.String(required=True, description='Meetup Title'),
        'description':fields.String(required=True, description='Meetup description'),
        'images':fields.String(description='Meetup images'),
        'Tags':fields.String(description='Meetup tags'),
        'createdOn':fields.Date(description='Created date'),
        'happeningOn':fields.String(required=True,description='When meetup will be held'),
        'host':fields.String(required=True, description='Who is hosting the meetup'),
        'hostFrom':fields.String(description='Where the host come from')

    })