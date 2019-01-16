"""
This file holds question model logic.
"""

import datetime
from flask_jwt_extended import jwt_required, get_current_user

# local imports
from api.v1.main.model.question import Question, QUESTIONS
from api.v1.main.service.meetup_service import get_specific_meetup_by_id
from api.v1.main.service.user_auth_service import UserAuth
from api.v1.main.service.user_service import get_user_by_email

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
    return QUESTIONS, 200

def save_new_question(question_data, meetup_id):
    """
    Save a new question.
    """
    title = question_data["title"]
    body = question_data["body"]
    votes = 0
    meetup = get_specific_meetup_by_id(meetup_id)
    user_id = UserAuth.get_user_id()
    is_admin = UserAuth.get_admin()

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

    if is_admin:
        response_object = {
            'status':401,
            'message':'Admin cannot create a question'
        }
        return response_object, 401
    else:
        new_question = Question()
        new_question.createdOn = datetime.datetime.utcnow()
        new_question.user_id = user_id 
        new_question.title = title
        new_question.body = body
        new_question.meetup_id = meetup.meetup_id
        new_question.votes=votes
        QUESTIONS.append(new_question)
        response_object = {
            'status':201,
            'message':'{}, Question has been created successfully'.format(title)
        }
        return response_object, 201

def specific_question(question_id):
    """
    Get a specific question.
    """
    question = get_question_by_id(question_id)
    if question:
        return question, 200
    if not question:
        response_object = {
            'status':404,
            'message':'Question you are looking for is nolonger there.'
        }
        return response_object, 404

def upvote_question(question_id):
    question = get_question_by_id(question_id)


    if question:
        
        print(question.votes)
        response_object = {
            'status':201,
            'message':'You have successfully upvoted this question'
        }
        return response_object, 201

    else:
        response_object = {
            'status':404,
            'message':'Question not available.'
        }
        return response_object, 404

def downvote_question(question_id):
    question = get_question_by_id(question_id)


    if question:
        question.votes-=1
        response_object = {
            'status':201,
            'message':'You have successfully downvoted this question'
        }
        return response_object, 201

    else:
        response_object = {
            'status':404,
            'message':'Question not available.'
        }
        return response_object, 404

        

