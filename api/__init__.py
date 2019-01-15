"""
Main entry point for the Api resources.
"""

from flask_restplus import Api
from flask import Blueprint

# local import
from api.v1.main.controller.user_controller import api as user_ns
from api.v1.main.controller.user_auth_controller import api as user_auth
from api.v1.main.controller.meetup_controller import api as meetup
from api.v1.main.controller.question_controller import api as quiz
from api.v1.main import creat_app

# blueprint instance
blueprint = Blueprint('api', __name__)

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(blueprint, authorizations=authorizations,
            title='QUESTIONER API',
            version='1',
            description='Crowd-source questions for a meetup. Questioner helps the' 
            +'meetup organizer prioritizequestions to be answered. Other users can vote'
            + 'on asked questions and they bubble to the topor bottom of the log.')

api.add_namespace(user_ns, path='/api/v1/user')
api.add_namespace(user_auth, path='/api/v1/user/auth')
api.add_namespace(meetup, path='/api/v1/meetup')
api.add_namespace(quiz, path='/api/v1/questions')
