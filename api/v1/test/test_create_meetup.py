"""
This file test create a meetup testcases.
"""

import datetime
from datetime import timedelta
import unittest
import json

# local imports
from api.v1.test.base_test import BaseTestCase

class TestCreateMeetUp(BaseTestCase):

    def test_succesful_crete_meetup(self):

        
        with self.client:
            """
            Test succesful book creation.
            """

            # signin admin
            self.admin_signin()
            # create a meetup
            response = self.create_meetup()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'success')
            self.assertTrue(result['message'] == 'Meetup has been created successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_unsuccesful_normal_user_create_meetup(self):
  
        with self.client:
            """
            Test regular user cannot creat a meetup
            """
            # signup user
            self.signup_user()
            # signin admin
            self.signin_user()
            # create a meetup
            response = self.create_meetup()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'To create a meetup you need to be an admin for your meetup')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)


    def test_succesful_crete_meetup_with_no_image(self):

        
        with self.client:
            """
            Test succesful book creation with no image.
            """

            # signin admin
            self.admin_signin()
            # create a meetup
            response = self.create_meetup_no_image()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'success')
            self.assertTrue(result['message'] == 'Meetup has been created successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_unsuccesful_meetup_with_no_topic(self):
  
        with self.client:
            """
            Test cannot create a meetup without a top
            """
            # signin admin
            self.admin_signin()
            response = self.create_meetup_no_topic()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Provide a topic for your meetup')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    
    def test_unsuccesful_meetup_with_no_description(self):
  
        with self.client:
            """
            Test cannot creat a meetup without a description
            """
            # signin admin
            self.admin_signin()
            response = self.create_meetup_no_topic()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Provide a description for your meetup')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_unsuccesful_duplicate_meetup(self):
  
        with self.client:
            """
            Test cannot creat a duplicate meetup
            """
            # signin admin
            self.admin_signin()
            # create meetup
            self.create_meetup()
            response = self.create_meetup()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'This meetup already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

if __name__ == '__main__':
    unittest.main()
