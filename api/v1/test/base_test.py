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

    # signin admin 2
    def admin_signin2(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='admin2@admin.com',
                password_hash='adm@3In'
            )),
            content_type='application/json'
        )

    # signout user
    def signout_user(self):
        return self.client.post(
            '/api/v1/user/auth/signout',
                data=json.dumps(dict(
                email='admin2@admin.com',
                password_hash='adm@3In'
            )),
            content_type='application/json'
        )

    # create_meetup
    def create_meetup(self):
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                topic= "meetup",
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

    # create_meetup_ 2
    def create_meetup_2(self):
        return self.client.post(
            '/api/v1/meetup/create',
                data=json.dumps(dict(
                topic= "Meetup 2",
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
                topic= "image",
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
                topic= "description",
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

    # def get specific meetup using meetup id
    def specific_meetup(self):
        return self.client.get(
            '/api/v1/meetup/1')

    # non existing meetup
    def unavailable_meetup(self):
        return self.client.get(
            '/api/v1/meetup/16')

    # non existing meetup
    def get_all_meetups_available(self):
        return self.client.get(
            '/api/v1/meetup/meetups')

    # question successfully
    def create_a_question(self):
        return self.client.post(
            '/api/v1/questions/create',
                data=json.dumps(dict(
                title="A sinple title",
                body="Just a very long text"
            )),
            content_type='application/json'
        )

    # question with no title
    def create_a_question_no_title(self):
        return self.client.post(
            '/api/v1/questions/create',
                data=json.dumps(dict(
                title="",
                body="Just a very long text",
                createdOn=datetime.datetime.utcnow
            )),
            content_type='application/json'
        )

    # question with no body
    def create_a_question_no_body(self):
        return self.client.post(
            '/api/v1/questions/create',
                data=json.dumps(dict(
                title="A sinple title",
                body="",
                createdOn=datetime.datetime.utcnow
            )),
            content_type='application/json'
        )

