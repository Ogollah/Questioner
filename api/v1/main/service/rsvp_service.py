
from api.v1.main.model.rvsp import Rsvp, RVSPS
from api.v1.main.service.user_auth_service import UserAuth
from api.v1.main.service.user_service import get_user_by_email
from api.v1.main.service.meetup_service import get_meetup_by_topic, get_specific_meetup_by_id

def get_rsvp_by_topic(topic):
    """
    Get Rsvp by topic.
    """
    for rsvp in RVSPS:
        if rsvp.topic == topic:
            return rsvp

def save_new_rsvp(meetup_id, user_input):
    rsvp_status = ['yes', 'no', 'maybe']
    valid_status = [x for x in rsvp_status]
    meetup = get_specific_meetup_by_id(meetup_id)
    
    status = user_input['status'].lower()
    meetup_id = meetup_id
    user_id = UserAuth.get_user_id()
    admin = UserAuth.get_admin()
    

    if meetup:
        topic = meetup.topic
    else:
        response_object = {
            'status':404,
            'message':'Meetup is not available.'
        }
        return response_object, 404

    rsvp = get_rsvp_by_topic(topic)

    if status == "":
        response_object = {
            'status':400,
            'message':'Provide a status (yes, no, or maybe).'
        }
        return response_object, 400

    if not valid_status:
        response_object = {
            'status':400,
            'message':'Provide a status (yes, no, or maybe).'
        }
        return response_object, 400

    if admin:
        response_object = {
            'status':401,
            'message':'Admin cannot reserve a meetup'
        }
        return response_object, 401

    if valid_status:
        if rsvp:
            response_object = {
                'status':409,
                'message':'You have already reserve this meetup {}'.format(topic)
            }
            return response_object, 409


        if status == "no":
            response_object = {
            'status':200,
            'message':'Meetup is not reserved.'
            }
            return response_object, 200
        
        if not rsvp:
            save_rsvp = Rsvp()
            save_rsvp.meetup_id = meetup_id
            save_rsvp.topic = topic
            save_rsvp.status = status
            save_rsvp.user_id = user_id

            RVSPS.append(save_rsvp)
            response_object = {
                'status':201,
                'message':'{}, Meetup has been successfully reserved'.format(topic)
            }
            return response_object, 201

