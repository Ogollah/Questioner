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

    # sign up user
    def signup_user(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='login@mail.com',
                username='example',
                password_hash='42qwR@#'
            )),
            content_type='application/json'
        )

    
    # signin user
    def signin_user(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='login@mail.com',
                password_hash='42qwR@#'
            )),
            content_type='application/json'
        )

    # signin admin
    def admin_signin(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='admin@admin.com',
                password_hash='adm@3In'
            )),
            content_type='application/json'
        )

    # create_meetup
    def create_meetup(self):
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                topic= "string",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4",
                host= "string",
                hostFrom= "string"
                )),
            content_type='application/json'
        )

    # meet without image
    def create_meetup_no_image(self):


        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                topic= "string",
                description= "string",
                images= "",
                Tags="string",
                createdOn= "string",
                happeningOn= "4",
                host= "string",
                hostFrom= "string"
            )),
            content_type='application/json'
        )

    # meetup without a topic

    def create_meetup_no_topic(self):

        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                topic= "",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4",
                host= "string",
                hostFrom= "string"
            )),
            content_type='application/json'
        )

    # meetup without description
    def create_meetup_no_description(self):
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                topic= "string",
                description= "",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4",
                host= "string",
                hostFrom= "string"
            )),
            content_type='application/json'
        )
