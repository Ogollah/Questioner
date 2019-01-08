"""
This file initialize the project.
"""

from flask import Flask

# local import
from api.v1.config import api_congig


def creat_app(config_name):
    api = Flask(__name__)
    api.config.from_object(api_congig[config_name])

    return api
