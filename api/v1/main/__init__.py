"""
This file initialize the project.
"""

from flask import Flask
from flask_bcrypt import Bcrypt

# local import
from api.v1.config import api_congig

bcrypt = Bcrypt()


def creat_app(config_name):
    api = Flask(__name__)
    api.config.from_object(api_congig[config_name])
    bcrypt.init_app(api)

    return api
