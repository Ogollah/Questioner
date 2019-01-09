"""
This file test user signin testcases.
"""

import unittest
import json

# local import
from api.v1.test.base_test import BaseTestCase

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

class TestUserSignin(BaseTestCase):
    def test_succesful_user_signin(self):

        # signup user
        signup_user(self)
        with self.client:
            """
            Test succesful signin.
            """
            # signup user
            response = signin_user(self)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'success')
            self.assertTrue(result['message'] == 'You have signed in successfully.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_signin_with_invalid_pass(self):
        with self.client:
            """
            Test signi with invalid password.
            """
            response = signin_invalid_pass(self)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Invalid password, please try again.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    
    def test_signin_with_invalid_email(self):
        with self.client:
            """
            Test signi with invalid email.
            """

            response = signin_invalid_email(self)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Invalid email, please try again.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

        
    def test_signin_non_registered_user(self):
        with self.client:
            """
            Test signi non registered user.
            """

            response = signin_non_registered_user(self)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'User not found, Kindly signup to user this service')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
