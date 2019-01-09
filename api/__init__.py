"""
Main entry point for the Api resources.
"""

from flask_restplus import Api
from flask import Blueprint

# local import
from api.v1.main.controller.user_controller import api as user_ns

# blueprint instance
blueprint = Blueprint('api', __name__)

api = Api(blueprint,
            title='QUESTIONER API',
            version='1.0',
            description='Crowd-source questions for a meetup. Questioner helps the' 
            +'meetup organizer prioritizequestions to be answered. Other users can vote'
            + 'on asked questions and they bubble to the topor bottom of the log.')

api.add_namespace(user_ns, path='/api/v1/user')
