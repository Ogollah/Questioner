"""
This file handles question related HTTP request.
"""

from flask import request
from flask_restplus import Resource

# local imports
from api.v1.main.util.question_dto import QuestionDto
from api.v1.main.service.question_service.question_service import save_new_question

api = QuestionDto.api
quiz = QuestionDto.question

@api.route('/<int:meetup_id>/create')
@api.param('meetup_id', 'Meetup Identification')
class CreateQuestion(Resource):

    @api.response(201, 'Question has been created successfully')
    @api.doc('Create a Question')
    @api.expect(quiz, validate=True)
    def post(self, meetup_id):
        """
        Create a Question
        """
        quiz_data = request.json
        return save_new_question(question_data=quiz_data, meetup_id=meetup_id)
