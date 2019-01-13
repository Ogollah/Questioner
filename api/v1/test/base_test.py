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
        return api# sign up user
    def signup_user_reg(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='mail@mail.com',
                username='example',
                password='42qwR@#'
            )),
            content_type='application/json'
        )

    # sign up user
    def signup_user_dub(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='example@example.com',
                username='example',
                password='42qwR@#'
            )),
            content_type='application/json'
        )

    # sign up user with invalid email
    def signup_user_invalid_email(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='mail.com',
                username='example',
                password='42qwR@#'
            )),
            content_type='application/json'
        )

    # sign up user with password with no numeric value
    def signup_user_password_no_number(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='nomail@mail.com',
                username='example',
                password='rtqwyM'
            )),
            content_type='application/json'
        )

    # sign up user with short password
    def signup_user_short_password(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='somail@mail.com',
                username='example',
                password='tyw'
            )),
            content_type='application/json'
        )

    # sign up user with long password
    def signup_user_long_password(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='lomail@mail.com',
                username='example',
                password='Longestpasswordfortestin#4'
            )),
            content_type='application/json'
        )

    # sign up user with password with no caps lock
    def signup_user_password_no_caps(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='cmail@mail.com',
                username='example',
                password='ytyyutututy'
            )),
            content_type='application/json'
        )

    # sign up user with no special character
    def signup_user_password_no_special_cha(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='spmail@mail.com',
                username='example',
                password='aaaaaaa'
            )),
            content_type='application/json'
        )

    # sign up user with no lower case
    def signup_user_password_no_lower_case(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='Lmail@mail.com',
                username='example',
                password='QWEASLLRE'
            )),
            content_type='application/json'
        )

    # sign up user with invalid username length of less than 4 character
    def signup_user_invalid_length(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Jhone',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='kmail@mail.com',
                username='ex',
                password='42qwRhjkh'
            )),
            content_type='application/json'
        )

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
                password='42qwR@#'
            )),
            content_type='application/json'
        )


    # sign up user 3
    def signup_user_3(self):
        return self.client.post(
            '/api/v1/user/signup',
                data=json.dumps(dict(
                firstname='Mary',
                lastname='Doe',
                othername='Johnson',
                phoneNumber='+25422034587',
                email='u3example@mail.com',
                username='example',
                password='42qwR@#'
            )),
            content_type='application/json'
        )

    # sign in user 3
    def signin_user_3(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='example@mail.com',
                password='42qwR@#'
            )),
            content_type='application/json'
        )

    
    # signin user
    def signin_user(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='login@mail.com',
                password='42qwR@#'
            )),
            content_type='application/json'
        )

    # signin admin
    def admin_signin(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='admin@admin.com',
                password='adm@3In'
            )),
            content_type='application/json'
        )

    # signin admin 2
    def admin_signin2(self):
        return self.client.post(
            '/api/v1/user/auth/signin',
                data=json.dumps(dict(
                email='admin2@admin.com',
                password='adm@3In'
            )),
            content_type='application/json'
        )

    # signout user
    def signout_user(self):
        return self.client.post(
            '/api/v1/user/auth/signout',
                data=json.dumps(dict(
                email='admin2@admin.com',
                password='adm@3In'
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
            '/api/v1/questions/1/create',
                data=json.dumps(dict(
                title="A sinple title",
                body="Just a very long text"
            )),
            content_type='application/json'
        )

    # question successfully
    def create_a_question_2(self):
        return self.client.post(
            '/api/v1/questions/1/create',
                data=json.dumps(dict(
                title="A sinple title",
                body="Just a very long text"
            )),
            content_type='application/json'
        )

    # question with no title
    def create_a_question_no_title(self):
        return self.client.post(
            '/api/v1/questions/1/create',
                data=json.dumps(dict(
                title="",
                body="Just a very long text",
                # createdOn=datetime.datetime.utcnow()
            )),
            content_type='application/json'
        )

    # question with no body
    def create_a_question_no_body(self):
        return self.client.post(
            '/api/v1/questions/1/create',
                data=json.dumps(dict(
                title="A sinple title",
                body="",
                # createdOn=datetime.datetime.utcnow()
            )),
            content_type='application/json'
        )

    # non existing meetup
    def get_all_questions_available(self):
        return self.client.get(
            '/api/v1/questions')

