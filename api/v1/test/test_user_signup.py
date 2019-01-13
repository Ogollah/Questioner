"""
This file tests user signup testcases.
"""

import unittest 
import json
import datetime

# local imports
from api.v1.main.model.user import User, USERS
from api.v1.test.base_test import BaseTestCase

class TestUserSignup(BaseTestCase):
    def test_succesful_user_signup(self):
        with self.client:
            """
            Test succesful signup.
            """
            # signup user
            response = self.signup_user_reg()
            print(response)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 201)
            self.assertTrue(result['message'] == 'You have signed up successfully.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_duplicate_signup(self):
        """
        Test user signup already signup user.
        """
        # signup user
        
        with self.client:
            self.signup_user_dub()
            response = self.signup_user_dub()
            print(response)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 409)
            self.assertTrue(result['message'] == 'User with this email address already exist.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_valid_email(self):
        """
        Test for email validity
        """
        with self.client:
            response = self.signup_user_invalid_email()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Check format of your email.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_max_password_length(self):
        """
        Password length.
        """

        with self.client:
            response = self.signup_user_long_password()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Password must be between 4 and 16 characters.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_min_password_length(self):
        """
        Password length.
        """

        with self.client:
            response = self.signup_user_short_password()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Password must be between 4 and 16 characters.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_special_character_password(self):
        """
        Password with no special character.
        """

        with self.client:
            response = self.signup_user_password_no_special_cha()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Password must contain a special character.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_lower_password(self):
        """
        Password with no special lowercase character.
        """

        with self.client:
            response = self.signup_user_password_no_lower_case()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Password should contain a lower case character')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_caps_password(self):
        """
        Password with no capital character.
        """

        with self.client:
            response = self.signup_user_password_no_caps()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Password should contain a capital letter')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_numb_password(self):
        """
        Password with no numeric value.
        """

        with self.client:
            response = self.signup_user_password_no_number()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Password should contain a number.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    
    def test_username_length(self):
        """
        Username length
        """

        with self.client:
            response = self.signup_user_invalid_length()
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Username must be between 4 and 15 characters')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
    