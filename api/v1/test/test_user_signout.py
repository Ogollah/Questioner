"""
This file holds user sighout test cases.
"""

import json
import unittest

# local import
from api.v1.test.base_test import BaseTestCase

class UserSignoutTestCases(BaseTestCase):

    def signup_user(self):
        
        return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            firstname='Jhone',
            lastname='Doe',
            othername='Johnson',
            phoneNumber='+25422034587',
            email='signout@mail.com',
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
            email='signout@mail.com',
            password='42qwR@#'
        )),
        content_type='application/json'
    )

    def test_successfull_signout(self):
        with self.client:
            """
            Test succesful signin.
            """
            self.signup_user()
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/user/auth/signout', headers=dict(Authorization=access_token),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 200)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
