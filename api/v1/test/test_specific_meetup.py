"""
This file holds test cases for getting a specific meetup.
"""

import unittest
import json

from api.v1.test.base_test import BaseTestCase

class TestSpecificmeetup(BaseTestCase):

    def test_succesful_get_specific_meetup(self):

    
        with self.client:
            """
            Test succesfuly get specific meetup
            """
            # signup user
            self.signup_user()
            
            # signin user
            self.signin_user
            response = self.specific_meetup()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'success')
            self.assertEqual(response.status_code, 200)

    def test_unavailable_meetup(self):

        with self.client:
            """
            Test user cannot get unavailable meetup
            """
            # signup user
            self.signup_user() 
            # signin user
            self.signin_user
            response = self.unavailable_meetup()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertEqual(response.status_code, 404)

    def test_only_signi_users_can_access_specifi_meetup(self):

        with self.client:
            """
            Test user cannot get specific meetup if not signed in
            """
            # signup user
            self.signup_user() 
            response = self.specific_meetup()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertEqual(response.status_code, 401)

