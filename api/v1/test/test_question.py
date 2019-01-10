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
            