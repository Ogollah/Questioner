"""
This file handles question related HTTP request.
"""

from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required

# local imports
from api.v1.main.util.question_dto import QuestionDto
from api.v1.main.service.question_service.question_service import save_new_question,get_all_questions

api = QuestionDto.api
quiz = QuestionDto.question

@api.route('/<int:meetup_id>/create')
@api.param('meetup_id', 'Meetup Identification')
class CreateQuestion(Resource):

    @api.response(201, 'Question has been created successfully')
    @api.doc('Create a Question')
    @api.expect(quiz, validate=True)
    @api.doc(security='Bearer Auth')
    @jwt_required
    def post(self, meetup_id):
        """
        Create a Question
        """
        quiz_data = request.json
        return save_new_question(question_data=quiz_data, meetup_id=meetup_id)

@api.route('/questions') 
@api.response(401, 'You need to login first')   
class GetMeetups(Resource):
    @api.doc('List of all available questions')
    @api.marshal_list_with(quiz, envelope='Questions')
    @api.doc(security='Bearer Auth')
    @jwt_required
    def get(self):
        """Get a list of all available questionss"""
        return  get_all_questions()
