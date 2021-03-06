"""
This file holds meetup model logic.
"""

import datetime
from datetime import timedelta
from flask_jwt_extended import jwt_required, get_current_user

# local imports
from api.v1.main.model.meetup import Meetup, MEETUPS
from api.v1.main.model.user import User, USERS
from api.v1.main.service.user_service import get_user_by_email
from api.v1.main.service.user_auth_service import UserAuth

def time_format(happeningOn):
    try:
        valid_time = datetime.datetime.strptime(happeningOn, '%Y-%m-%d %H:%M')

        return valid_time
    except Exception as exc:
        print(exc)
        return None

def get_meetup_by_topic(topic):
    """
    Get a meetup by topic.
    """
    for meetup in MEETUPS:
        if meetup.topic == topic:
            return meetup

def get_specific_meetup_by_id(meetup_id):
    """
    Get specific meetup using meetup id.
    """
    for meetup in MEETUPS:
        if meetup.meetup_id == meetup_id:
            return meetup

def save_new_meetup(meetup_data):
    # get meetup data
    topic = meetup_data["topic"]
    description = meetup_data["description"]
    images = meetup_data["images"]
    Tags = meetup_data["Tags"]
    host=meetup_data["host"]
    hostFrom=meetup_data["hostFrom"]
    createdOn = datetime.datetime.utcnow()
    happeningOn =time_format(happeningOn=meetup_data["happeningOn"])

    meetup = get_meetup_by_topic(topic=topic)
    is_admin = UserAuth.get_admin()

    if not happeningOn:
        response_object = {
            'status':400,
            'message':'Use correct format OF date and time (YY-MM-DD HH:MM)'
        }
        return response_object, 400
    
    if not topic:
        response_object = {
            'status':400,
            'message':'Provide a topic for your meetup'
        }
        return response_object, 400

    
    if meetup:
        response_object = {
            'status':409,
            'message':'This meetup already exists.'
        }
        return response_object, 409

    if not description:
        response_object = {
            'status':400,
            'message':'Provide a description for your meetup'
        }
        return response_object, 400

    if  is_admin and not meetup:
        new_meetup = Meetup()
        new_meetup.topic=topic
        new_meetup.description=description
        new_meetup.happeningOn=happeningOn
        new_meetup.images=images
        new_meetup.Tags=Tags
        new_meetup.createdOn=createdOn
        new_meetup.host=host
        new_meetup.hostFrom=hostFrom
        MEETUPS.append(new_meetup)
        saved_meetup = {
                'meetup_id':new_meetup.meetup_id,
                'topic':new_meetup.topic,
                'description':new_meetup.description,
                'happeningOn':str(new_meetup.happeningOn),
                'images':new_meetup.images,
                'Tags':new_meetup.Tags,
                'host':new_meetup.host,
                'hostFrom':new_meetup.hostFrom,
                'createdOn':str(new_meetup.createdOn)
                }
        response_object = {
            'status':201,
            'data':saved_meetup,
            'message':'{}, Meetup has been created successfully'.format(topic)
        }
        return response_object, 201
    else:
        response_object = {
            'status':401,
            'message':'Only admin can perform this operation.'
        }
        return response_object, 401

def accessing_meetup(meetup_id):
    meetup = get_specific_meetup_by_id(meetup_id)

    if meetup:
        return meetup, 200
    else:
        response_object = {
            'status':404,
            'message':'Meetup not found in the database'
        }
        return response_object, 404
        

def get_all_meetups():
    """
    Get a list of all meetups.
    """
    return MEETUPS, 200  

def update_meetup(meetup_data, meetup_id):
    """
    Update a meetup.
    """
    meetup = get_specific_meetup_by_id(meetup_id)
    admin = UserAuth.get_admin()

    topic = meetup_data["topic"]
    description = meetup_data["description"]
    images = meetup_data["images"]
    Tags = meetup_data["Tags"]
    createdOn = datetime.datetime.utcnow()
    happeningOn = time_format(happeningOn=meetup_data["happeningOn"])
    host=meetup_data['host']
    hostFrom=meetup_data['hostFrom']

    if meetup:

        if not happeningOn:
            response_object = {
                'status':400,
                'message':'Use correct format OF date and time (YY-MM-DD HH:MM)'
            }
            return response_object, 400
    
        if not topic:
            response_object = {
                'status':400,
                'message':'Provide a topic for your meetup'
            }
            return response_object, 400

        if not description:
            response_object = {
                'status':400,
                'message':'Provide a description for your meetup'
            }
            return response_object, 400

        if admin:
            meetup.topic=topic
            meetup.description=description
            meetup.images=images
            meetup.Tags=Tags
            meetup.createdOn=createdOn
            meetup.happeningOn=happeningOn
            meetup.host=host
            meetup.hostFrom=hostFrom

            update_meetup = {
                'meetup_id':meetup.meetup_id,
                'topic':meetup.topic,
                'description':meetup.description,
                'happeningOn':str(meetup.happeningOn),
                'images':meetup.images,
                'Tags':meetup.Tags,
                'host':meetup.host,
                'hostFrom':meetup.hostFrom
            }

            response_object = {
            'status':200,
            'data':update_meetup,
            'message':'Meetup updated successfully'
            }
            return response_object, 200

        else:
            response_object = {
            'status':401,
            'message':'Only admin can update a meetup'
            }
            return response_object, 401
    else:
        response_object = {
            'status':404,
            'message':'No meetup record in the database'
        }
        return response_object, 404

def delete_meetup(meetup_id):
    """
    Delete a meetup.
    """
    available_meetup = get_specific_meetup_by_id(meetup_id)
    user_admin = UserAuth.get_admin()

    if available_meetup:
        if user_admin:
            MEETUPS.remove(available_meetup)
            response_object = {
            'status':200,
            'message':'Meetup deleted successfully'
            }
            return response_object, 200

        else:
            response_object = {
            'status':401,
            'message':'You need to be admin to perform this operation'
            }
            return response_object, 401
    else:
        response_object = {
            'status':404,
            'message':'Meetup you are looking for is not available'
        }
        return response_object, 404
