
from flask_restplus import Namespace, fields

class QuestionDto:
    """
    Question details.
    """

    api = Namespace('Question Crude Operation', description='Question operations')
    question = api.model('question',{
        'question_id':fields.Integer(description='Question Identification'),
        'title':fields.String(required=True, description='Question Title'),
        'body':fields.String(required=True, description='Question Body'),
        'createdOn':fields.Date(description='Question Created Date'),
        'meetup_id':fields.Integer(description='Meetup Identification'),
        'votes':fields.Integer(description='Question votes'),
        'user_id':fields.Integer(description='User Identification')
    })