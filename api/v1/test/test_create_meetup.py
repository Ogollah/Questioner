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


    def setUp(self):
        self.meetup_data =dict(
                topic= "meetup",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4/11/2019",
                host= "string",
                hostFrom= "string"
                )

        self.meetup_data_normal =dict(
                topic= "Normal",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4/11/2019",
                host= "string",
                hostFrom= "string"
                )
        self.meetup_data_no_image =dict(
                topic= "image",
                description= "string",
                images= "",
                Tags="string",
                createdOn= "string",
                happeningOn="4/11/2019",
                host= "string",
                hostFrom= "string"
                )

        self.meetup_data_no_topic =dict(
                topic= "",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4/11/2019",
                host= "string",
                hostFrom= "string"
                )

        self.meetup_data_no_desc =dict(
                topic= "description",
                description= "",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "4/11/2019",
                host= "string",
                hostFrom= "string"
                )
    

    def signup_user(self):
        
        return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            firstname='Jhone',
            lastname='Doe',
            othername='Johnson',
            phoneNumber='+25422034587',
            email='meetup@mail.com',
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
            email='meetup@mail.com',
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


    def test_succesful_crete_meetup(self):

        
        with self.client:
            """
            Test succesful meetup creation.
            """
            
            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/meetup/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 201)
            self.assertTrue(result['message'] == 'Meetup has been created successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    # def test_unsuccesful_normal_user_create_meetup(self):
  
    #     with self.client:
    #         """
    #         Test regular user cannot creat a meetup
    #         """
    #         self.signup_user()
    #         resp = self.login_user()
    #         access_token = json.loads(resp.data.decode())['access_token'] 
    #         response = self.client.post('/api/v1/meetup/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data_normal),content_type='application/json')
    #         # return result in json format
    #         result = json.loads(response.data.decode())
    #         print(result)
    #         self.assertTrue(result['status'] == '401')
    #         self.assertTrue(result['message'] == 'To create a meetup you need to be an admin for your meetup')
    #         self.assertTrue(response.content_type == 'application/json')
    #         self.assertEqual(response.status_code, 401)


    def test_succesful_crete_meetup_with_no_image(self):

        
        with self.client:
            """
            Test succesful book creation with no image.
            """
            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/meetup/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data_no_image),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 201)
            self.assertTrue(result['message'] == 'Meetup has been created successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_unsuccesful_meetup_with_no_topic(self):
  
        with self.client:
            """
            Test cannot create a meetup without a topic
            """
            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/meetup/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data_no_topic),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Provide a topic for your meetup')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    
    def test_unsuccesful_meetup_with_no_description(self):
  
        with self.client:
            """
            Test cannot creat a meetup without a description
            """

            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/meetup/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data_no_desc),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Provide a description for your meetup')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_unsuccesful_duplicate_meetup(self):
  
        with self.client:
            """
            Test cannot creat a duplicate meetup
            """
            
            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token'] 
            response = self.client.post('/api/v1/meetup/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data),content_type='application/json')
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 409)
            self.assertTrue(result['message'] == 'This meetup already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

if __name__ == '__main__':
    unittest.main()
