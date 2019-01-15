"""
This file holds meetups test cases.
"""

import unittest
import json

# local imports
from api.v1.test.base_test import BaseTestCase

class MeetupsTestCases(BaseTestCase):

    def signup_user(self):
        
        return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            firstname='Jhone',
            lastname='Doe',
            othername='Johnson',
            phoneNumber='+25422034587',
            email='meetups@mail.com',
            username='example',
            password='42qwR@#'
        )),
        content_type='application/json'
    )
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

    def test_successful_get_all_meetups(self):
        with self.client:
            """
            Test succesfuly get a list of all meetups
            """
            self.signup_user()
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.get('/api/v1/meetup/meetups', headers=dict(Authorization=access_token),content_type='application/json')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
