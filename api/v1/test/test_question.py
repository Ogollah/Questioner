"""
This file holds question related test cases.
"""

import unittest
import json
import datetime

# local imports
from api.v1.test.base_test import BaseTestCase

class TestCreateQuestion(BaseTestCase):

    def test_succesful_crete_question(self):

        
        with self.client:
            """
            Test succesful question creation.
            """
            # signup user
            self.signup_user()

            # signin user
            self.signin_user()
            # create a question
            response = self.create_a_question()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'success')
            self.assertTrue(result['message'] == 'Question has been created successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    
    def test_unsuccessful_create_question_with_no_title(self):  
        with self.client:
            """
            Test user cannot create a question with no title.
            """
            # signup user
            self.signup_user()
            # signin user
            self.signin_user()
            # create a question
            response = self.create_a_question_no_title()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'A title is need to create a question.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)
      
    def test_unsuccessful_create_question_with_no_body(self):  
        with self.client:
            """
            Test user cannot create a question with no body.
            """
            # signup user
            self.signup_user()
            # signin user
            self.signin_user()
            # create a question
            response = self.create_a_question_no_body()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'A body is need to create a question.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

          
    def test_admin_can_not_create_question(self):  
        with self.client:
            """
            Test user admin canot create a question.
            """
            
            # signin user admin
            self.admin_signin()
            # create a question
            response = self.create_a_question()
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 'fail')
            self.assertTrue(result['message'] == 'Admin cannot create a question')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)
