"""
This file holds question related test cases.
"""

import unittest
import json
import datetime

# local imports
from api.v1.test.base_test import BaseTestCase

class TestCreateQuestion(BaseTestCase):
    def setUp(self):
        self.question_data = dict(
                title="A sinple title",
                body="Just a very long text"
            )

        self.question_data_no_title = dict(
                title="",
                body="Just a very long text"
            )

        self.question_data_no_body = dict(
                title="A sinple title",
                body=""
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

    def login_user_admin(self):
        """This helper method helps log in a test user."""
        return self.client.post(
        '/api/v1/user/auth/signin',
            data=json.dumps(dict(
            email='admin@admin.com',
            password='#Sadm@3In'
        )),
        content_type='application/json'
    )

    def test_succesful_crete_question(self):

        
        with self.client:
            """
            Test succesful question creation.
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 201)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    
    def test_unsuccessful_create_question_with_no_title(self):  
        with self.client:
            """
            Test user cannot create a question with no title.
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data_no_title),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'A title is need to create a question.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)
      
    def test_unsuccessful_create_question_with_no_body(self):  
        with self.client:
            """
            Test user cannot create a question with no body.
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data_no_body),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'A body is need to create a question.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

          
    def test_admin_can_not_create_question(self):  
        with self.client:
            """
            Test user admin canot create a question.
            """
            
            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json')
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 401)
            self.assertTrue(result['message'] == 'Admin cannot create a question')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)
            
class TestAccessQuestion(BaseTestCase):
    def setUp(self):
        self.question_data = dict(
                title="A That simple title",
                body="Just a very long text"
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
    def test_successful_get_all_questions(self):
        with self.client:
            """
            Test succesfuly get a list of all questions
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token']
            self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json') 
            response = self.client.get('/api/v1/questions/questions', headers=dict(Authorization=access_token),content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_access_specific_question(self):
        with self.client:
            """
            Test succesfuly get a specific question
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json') 
            response = self.client.get('/api/v1/questions/1', headers=dict(Authorization=access_token),content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_can_not_access_specific_question(self):
        with self.client:
            """
            Test unavailable question
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.get('/api/v1/questions/16', headers=dict(Authorization=access_token),content_type='application/json')
            self.assertEqual(response.status_code, 404)

    def test_successful_upvote(self):
        with self.client:
            """
            Test successful upvoting a question.
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json') 
            response = self.client.post('/api/v1/questions/1/upvote', headers=dict(Authorization=access_token),content_type='application/json') 
            self.assertEqual(response.status_code, 201)

    
    def test_upvote_unavailable_question(self):
        with self.client:
            """
            Test trying to vote unavailable question
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json') 
            response = self.client.post('/api/v1/questions/18/upvote', headers=dict(Authorization=access_token),content_type='application/json') 
            self.assertEqual(response.status_code, 404)

    def test_successful_downvote(self):
        with self.client:
            """
            Test successful downvoting a question.
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json') 
            response = self.client.post('/api/v1/questions/1/downvote', headers=dict(Authorization=access_token),content_type='application/json') 
            self.assertEqual(response.status_code, 201)

    
    def test_downvote_unavailable_question(self):
        with self.client:
            """
            Test trying to vote unavailable question
            """
            resp = self.login_user()
            access_token = json.loads(resp.data.decode())['access_token'] 
            self.client.post('/api/v1/questions/1/create', headers=dict(Authorization=access_token),data=json.dumps(self.question_data),content_type='application/json') 
            response = self.client.post('/api/v1/questions/18/downvote', headers=dict(Authorization=access_token),content_type='application/json') 
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
