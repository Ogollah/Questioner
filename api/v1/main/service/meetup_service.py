"""
This file holds meetup model logic.
"""

import datetime
from datetime import timedelta

# local imports
from api.v1.main.model.meepup import Meetup, MEETUPS
from api.v1.main.model.user import User, USERS
from api.v1.main.service.user_auth_service import UserAuth

def get_meetup_by_topic(topic):
    """
    Get a meetup by topic.
    """
    for meetup in MEETUPS:
        if meetup.topic == topic:
            return meetup

def get_user_admin(admin):
    """
    Get admin
    """
    for user in USERS:
        if user.isAdmin == True:
            return user


def create_future_date(date_data):
    """
    Create When meetup will take place.
    """
    now = datetime.datetime.now()
    difference = datetime.timedelta(days=date_data)
    time = now + difference
    future = time.strftime("%m/%d/%Y")
    return future

def save_new_meetup(meetup_data):
    # get meetup data
    topic = meetup_data["topic"]
    description = meetup_data["description"]
    image = meetup_data["image"]
    Tags = meetup_data["Tags"]
    createdOn = datetime.datetime.utcnow()
    happeningOn = create_future_date(date_data=meetup_data["happeningOn"])

    meetup = get_meetup_by_topic(topic=topic)

    if topic == "":
        response_object = {
            'status':'fail',
            'message':'Provide a topic for your meetup'
        }
        return response_object, 401

    if description== "":
        response_object = {
            'status':'fail',
            'message':'Provide a description for your meetup'
        }
        return response_object, 401

    if meetup:
        response_object = {
            'status':'fail',
            'message':'This meetup already exists.'
        }
        return response_object, 409

    else:
        new_meetup = Meetup()
        new_meetup.topic=topic
        new_meetup.description=description
        new_meetup.happeningOn=happeningOn
        new_meetup.images=image
        new_meetup.Tags=Tags
        new_meetup.createdOn=createdOn
        MEETUPS.append(new_meetup)
        response_object = {
            'status':'fail',
            'message':'Meetup has been created successfully'
        }
        return response_object, 200

