"""
This is the base test of the api application, setting test environment
"""

from flask_testing import TestCase
import json
import datetime
from datetime import timedelta

# local imports
from manage import api

class BaseTestCase(TestCase):
    def create_app(self):
        api.config.from_object('api.v1.config.TestingConfig')
        return api
        