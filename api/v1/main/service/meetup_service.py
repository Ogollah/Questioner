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

def create_future_date(date_data):
    """
    Create When meetup will take place.
    """ 

def save_new_meetup(meetup_data):
    # get meetup data
    topic = meetup_data["topic"]
    description = meetup_data["description"]
    images = meetup_data["images"]
    Tags = meetup_data["Tags"]
    createdOn = datetime.datetime.utcnow()
    happeningOn = meetup_data["happeningOn"]

    meetup = get_meetup_by_topic(topic=topic)
    is_admin = UserAuth.get_admin

    if happeningOn == "":
        response_object = {
            'status':400,
            'message':'Provide the number of days to meetup day'
        }
        return response_object, 400

    if meetup:
        response_object = {
            'status':409,
            'message':'This meetup already exists.'
        }
        return response_object, 409

    if not is_admin and not meetup:
        response_object = {
            'status':401,
            'message':'To create a meetup you need to be an admin for your meetup'
        }
        return response_object, 401


    if topic == "":
        response_object = {
            'status':400,
            'message':'Provide a topic for your meetup'
        }
        return response_object, 400

    if description== "":
        response_object = {
            'status':400,
            'message':'Provide a description for your meetup'
        }
        return response_object, 400

    if  is_admin:
        new_meetup = Meetup()
        new_meetup.topic=topic
        new_meetup.description=description
        new_meetup.happeningOn=happeningOn
        new_meetup.images=images
        new_meetup.Tags=Tags
        new_meetup.createdOn=createdOn
        MEETUPS.append(new_meetup)
        response_object = {
            'status':201,
            'message':'{}, Meetup has been created successfully'.format(topic)
        }
        return response_object, 201

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

        