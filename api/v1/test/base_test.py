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
                password_hash='admin'
            )),
            content_type='application/json'
        )

    # create_meetup
    def create_meetup(self):
        days = 6
        now = datetime.datetime.now()
        difference = datetime.timedelta(days=days)
        
        happening = now+difference
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                location='Nairobi',
                images=['image1', 'image2'],
                topic='Hello World',
                happeningOn=happening,
                tags=['tag1', 'tag2', 'tag3'],
                description='Why do we limit the extensions that are allowed? You probably don’t want your users to be able to upload everything there if the server is directly sending out the data to the client.'
            )),
            content_type='application/json'
        )

    # meet without image
    def create_meetup_no_image(self):

        # future date
        days = 6
        now = datetime.datetime.now()
        difference = datetime.timedelta(days=days)
        happening = now+difference
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                location='Nairobi',
                images=[],
                topic='Python Marathon',
                happeningOn=happening,
                tags=['tag1', 'tag2', 'tag3'],
                description='Why do we limit the extensions that are allowed? You probably don’t want your users to be able to upload everything there if the server is directly sending out the data to the client.'
            )),
            content_type='application/json'
        )

    # meetup without a topic

    def create_meetup_no_topic(self):

        # future date
        days = 6
        now = datetime.datetime.now()
        difference = datetime.timedelta(days=days)
        happening = now+difference
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                location='Nairobi',
                images=['image1', 'image2'],
                topic='',
                happeningOn=happening,
                tags=['tag1', 'tag2', 'tag3'],
                description='Why do we limit the extensions that are allowed? You probably don’t want your users to be able to upload everything there if the server is directly sending out the data to the client.'
            )),
            content_type='application/json'
        )

    # meetup without description
    def create_meetup_no_description(self):

        # future date
        days = 6
        now = datetime.datetime.now()
        difference = datetime.timedelta(days=days)
        happening = now+difference
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                location='Nairobi',
                images=['image1', 'image2'],
                topic='Amazing',
                happeningOn=happening,
                tags=['tag1', 'tag2', 'tag3'],
                description=''
            )),
            content_type='application/json'
        )
