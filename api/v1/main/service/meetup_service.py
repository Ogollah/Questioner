"""
This file holds meetup model logic.
"""

import datetime
from datetime import timedelta

# local imports
from api.v1.main.model.meepup import Meetup, MEETUPS
from api.v1.main.model.user import User, USERS
from api.v1.main.service.user_service import get_user_by_email
from api.v1.main.service.user_auth_service import UserAuth, SIGNIN_USERS

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
    

def current_user():
    for user in SIGNIN_USERS:
        return user.isAdmin

def current_normal_user():
    for user in SIGNIN_USERS:
        return user

def create_future_date(date_data):
    """
    Create When meetup will take place.
    """
    now = datetime.datetime.now()
    difference = datetime.timedelta(days=date_data)
    time = now + difference
    return time

def save_new_meetup(meetup_data):
    # get meetup data
    topic = meetup_data["topic"]
    description = meetup_data["description"]
    images = meetup_data["images"]
    Tags = meetup_data["Tags"]
    createdOn = datetime.datetime.utcnow()
    happeningOn = create_future_date(date_data=int(meetup_data["happeningOn"]))

    meetup = get_meetup_by_topic(topic=topic)
    user = current_user()

    if meetup:
        response_object = {
            'status':'fail',
            'message':'This meetup already exists.'
        }
        return response_object, 409

    if not user:
        response_object = {
            'status':'fail',
            'message':'To create a meetup you need to be an admin for your meetup'
        }
        return response_object, 401


    if topic == "":
        response_object = {
            'status':'fail',
            'message':'Provide a topic for your meetup'
        }
        return response_object, 400

    if description== "":
        response_object = {
            'status':'fail',
            'message':'Provide a description for your meetup'
        }
        return response_object, 400

    if user and not meetup:
        new_meetup = Meetup()
        new_meetup.topic=topic
        new_meetup.description=description
        new_meetup.happeningOn=happeningOn
        new_meetup.images=images
        new_meetup.Tags=Tags
        new_meetup.createdOn=createdOn
        MEETUPS.append(new_meetup)
        response_object = {
            'status':'success',
            'message':'Meetup has been created successfully'
        }
        return response_object, 201

def accessing_meetup(meetup_id):
    user = current_normal_user()
    meetup = get_specific_meetup_by_id(meetup_id)

    if not user :
        response_object = {
            'status':'fail',
            'message':'Signin to access this resource'
        }
        return response_object, 401

    if user and not meetup:
        response_object = {
            'status':'fail',
            'message':'Meetup not found in the database'
        }
        return response_object, 404

    if user and meetup:
        return meetup, 200

def get_all_meetups():
    """
    Get a list of all meetups.
    """
    user = current_normal_user()
    if user:
        return MEETUPS  

    else:
        response_object = {
            'status':'fail',
            'message':'You need to login first.'
        }
        return response_object, 401
        