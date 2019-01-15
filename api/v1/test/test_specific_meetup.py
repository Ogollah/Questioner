"""
This file holds test cases for getting a specific meetup.
"""

import unittest
import json

from api.v1.test.base_test import BaseTestCase

class TestSpecificmeetup(BaseTestCase):

    def login_user(self):
        """This helper method helps log in a test user."""
        return self.client.post(
        '/api/v1/user/auth/signin',
            data=json.dumps(dict(
            email='meetups@mail.com',
            password='42qwR@#'
        )),
        content_type='application/json'
    )

    def test_succesful_get_specific_meetup(self):
        with self.client:
            """
            Test succesfuly get specific meetup
            """
            # self.signup_user()
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.get('/api/v1/meetup/meetups', headers=dict(Authorization=access_token),content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_unavailable_meetup(self):

        with self.client:
            """
            Test user cannot get unavailable meetup
            """
            # self.signup_user()
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.get('/api/v1/meetup/13', headers=dict(Authorization=access_token),content_type='application/json')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
