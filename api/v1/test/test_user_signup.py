"""
This file tests user signup testcases.
"""

import unittest 
import json
import datetime

# local imports
from api.v1.main.model.user import User, USERS
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
            email='mail.com',
            username='example',
            password='rtqwyt@#'
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
            email='mail.com',
            username='example',
            password='4qR@#'
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
            email='mail.com',
            username='example',
            password='Longestpasswordfor testin#4'
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
            email='mail.com',
            username='example',
            password='42qwyt@#'
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
            email='mail.com',
            username='example',
            password='42qwRhjkh'
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
            email='mail.com',
            username='example',
            password='QWEAS#33Y'
        )),
        content_type='application/json'
    )

# sign up user with invalid username length of less than 4 character
def signup_user_invalid_length(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            firstname='Jho',
            lastname='Doe',
            othername='Johnson',
            phoneNumber='+25422034587',
            email='mail.com',
            username='example',
            password='42qwRhjkh'
        )),
        content_type='application/json'
    )

class TestUserSignup(BaseTestCase):
    def test_succesful_user_signup(self):
        with self.client:
            """
            Test succesful signup.
            """
            # signup user
            response = signup_user(self)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'success')
            self.assertTrue(result['message'] == 'You have signed up successfully.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_duplicate_signup(self):
        """
        Test user signup already signup user.
        """
        # signup user
        signup_user(self)
        with self.client:
            response = signup_user(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'User with this email address already exist.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_valid_email(self):
        """
        Test for email validity
        """
        with self.client:
            response = signup_user_invalid_email(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Check format of your email.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_max_password_length(self):
        """
        Password length.
        """

        with self.client:
            response = signup_user_long_password(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Password should not be more than 16 characters.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_min_password_length(self):
        """
        Password length.
        """

        with self.client:
            response = signup_user_short_password(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Password should not be less than 6 characters.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_special_character_password(self):
        """
        Password with no special character.
        """

        with self.client:
            response = signup_user_password_no_special_cha(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Password should contain a special character.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_lower_password(self):
        """
        Password with no special lowercase character.
        """

        with self.client:
            response = signup_user_password_no_lower_case(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Password should contain a lower case character')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_caps_password(self):
        """
        Password with no capital character.
        """

        with self.client:
            response = signup_user_password_no_caps(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Password should contain a capital letter')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_numb_password(self):
        """
        Password with no numeric value.
        """

        with self.client:
            response = signup_user_password_no_number(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Password should contain atleast one number/ integer.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    
    def test_username_length(self):
        """
        Username length
        """

        with self.client:
            response = signup_user_password_no_number(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Username not be less than 4 characters.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
    