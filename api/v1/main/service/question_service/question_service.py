"""
This file holds question model logic.
"""

import datetime

# local imports
from api.v1.main.model.question import Question, QUESTIONS
from api.v1.main.service.meetup_service import current_normal_user, current_user, get_specific_meetup_by_id
from api.v1.main.service.user_auth_service import UserAuth, SIGNIN_USERS

def get_question_by_id(question_id):
    """
    Get question by question id
    """
    for question in QUESTIONS:
        if question.question_id == question_id:
            return question

def get_all_questions():
    """
    Get all available questions.
    """
    user = current_normal_user()
    if user:
        return QUESTIONS, 200
    else:
        response_object = {
            'status':'fail',
            'message':'You need to login first.'
        }
        return response_object, 401

def save_new_question(question_data, meetup_id):
    """
    Save a new question.
    """
    title = question_data["title"]
    body = question_data["body"]
    admin_user = current_user()
    user = current_normal_user()
    meetup = get_specific_meetup_by_id(meetup_id)

    if title == "":
        response_object = {
            'status':400,
            'message':'A title is need to create a question.'
        }
        return response_object, 400

    if body == "":
        response_object = {
            'status':400,
            'message':'A body is need to create a question.'
        }
        return response_object, 400

    if not user:
        response_object = {
            'status':401,
            'message':'Loggin to post a question.'
        }
        return response_object, 401

    if admin_user:
        response_object = {
            'status':401,
            'message':'Admin cannot create a question'
        }
        return response_object, 401
    else:
        new_question = Question()
        new_question.createdOn = datetime.datetime.utcnow()
        new_question.meetup_id = user.user_id
        new_question.title = title
        new_question.body = body
        new_question.meetup_id = meetup.meetup_id
        QUESTIONS.append(new_question)
        response_object = {
            'status':201,
            'message':'Question has been created successfully'
        }
        return response_object, 201
