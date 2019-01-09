"""
This file test user signin testcases.
"""

import unittest
import json

# sign up user
def signup_user(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            firstname='Jhone',
            lastname='Doe',
            othername='Johnson',
            phoneNumber='+25422034587',
            email='mail@mail.com',
            username='example',
            password_hash='42qwR@#'
        )),
        content_type='application/json'
    )

# signin user
def signin_user(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            email='mail@mail.com',
            password_hash='42qwR@#'
        )),
        content_type='application/json'
    )

# wrong password
def signin_invalid_pass(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            email='mail@mail.com',
            password_hash='wrongpass'
        )),
        content_type='application/json'
    )

# wrong email
def signin_invalid_email(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            email='invalid@mail.com',
            password_hash='wrongpass'
        )),
        content_type='application/json'
    )

# non registered user
def signin_non_registered_user(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            email='invalid@mail.com',
            password_hash='wrongpass'
        )),
        content_type='application/json'
    )


