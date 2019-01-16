from flask_restplus import Namespace, fields

class RsvpDto:
    """
    Reservation details.
    """

    api = Namespace('Meetup reservation', description='Reserves operations')
    rsvp = api.model('rsvp',{
        'rsvp_id':fields.Integer(description='Reserve Identification'),
        'topic':fields.String(description='Meetup Title'),
        'status':fields.String(required=True, description='Attendance Status'),
        'meetup_id':fields.Integer(description='Meetup Identification'),
        'user_id':fields.Integer(description='User Identification')
    })
    