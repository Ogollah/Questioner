"""
This file holds user sighout test cases.
"""

import json
import unittest

# local import
from api.v1.test.base_test import BaseTestCase
class UserSignoutTestCases(BaseTestCase):

    def test_successfull_signout(self):
        with self.client:
            """
            Test succesful signin.
            """
            # signup user
            self.signup_user()
            # signin user
            self.signin_user()

            # signout user
            response = self.signout_user()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 200)
            self.assertTrue(result['message'] == 'You have signedout successfully.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
