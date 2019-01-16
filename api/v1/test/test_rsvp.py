"""
This file is for testing rsvp test cases.
"""
import unittest
import json

#local imports
from api.v1.test.base_test import BaseTestCase

class TestRsvpTestCases(BaseTestCase):
    def setUp(self):
        self.meetup_data =dict(
                topic= "Reserve",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "2018-06-29 08:15:27",
                host= "string",
                hostFrom= "string"
                )

        self.meetup_data_succ =dict(
                topic= "success",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "2018-06-29 08:15:27",
                host= "string",
                hostFrom= "string"
                )

        self.meetup_data_no =dict(
                topic= "status",
                description= "string",
                images= "string",
                Tags="string",
                createdOn= "string",
                happeningOn= "2018-06-29 08:15:27",
                host= "string",
                hostFrom= "string"
                )

        self.status =dict(
                status= "yes",
                )

        self.status_no =dict(
                status= "no",
                )

        self.status_nill =dict(
                status= "",
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

    def test_successful_reserve_meetup(self):
        with self.client:
                """
                Test succesfuly reserve a meetup
                """
                resp = self.login_user()
                admin_login = self.login_user_admin()
                admin_header = json.loads(resp.data.decode())['access_token']
                access_token = json.loads(resp.data.decode())['access_token']
                rt = self.client.post('/api/v1/meetups/create', headers=dict(Authorization=admin_header),data=json.dumps(self.meetup_data_succ),content_type='application/json')
                response = self.client.post('api/v1/meetups/2/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status),content_type='application/json')
                result = json.loads(response.data.decode())
                self.assertTrue(result['status'] == 201)
                self.assertEqual(response.status_code, 201)

    
    def test_duplicate_reserve_meetup(self):
        with self.client:
                """
                Test can not rsvp duplicate meetups
                """
                resp = self.login_user()
                admin_login = self.login_user_admin()
                admin_header = json.loads(resp.data.decode())['access_token']
                access_token = json.loads(resp.data.decode())['access_token']
                rt = self.client.post('/api/v1/meetups/create', headers=dict(Authorization=admin_header),data=json.dumps(self.meetup_data),content_type='application/json')
                self.client.post('api/v1/meetups/1/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status),content_type='application/json')
                response = self.client.post('api/v1/meetups/1/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status),content_type='application/json')
                result = json.loads(response.data.decode())
                self.assertTrue(result['status'] == 409)
                self.assertEqual(response.status_code, 409)

        
    
    def test_unavailable_meetup(self):
        with self.client:
                """
                Test unavailable meetup can not be reserved
                """
                resp = self.login_user()
                admin_login = self.login_user_admin()
                admin_header = json.loads(resp.data.decode())['access_token']
                access_token = json.loads(resp.data.decode())['access_token']
                rt = self.client.post('/api/v1/meetups/create', headers=dict(Authorization=admin_header),data=json.dumps(self.meetup_data_no),content_type='application/json')
                response = self.client.post('api/v1/meetups/30/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status_no),content_type='application/json')
                result = json.loads(response.data.decode())
                self.assertTrue(result['status'] == 404)
                print(response)
                self.assertEqual(response.status_code, 404)

    def test_status_no(self):
        with self.client:
                """
                Test status no can not reserve meetup
                """
                resp = self.login_user()
                admin_login= self.login_user_admin()
                admin_header = json.loads(admin_login.data.decode())['access_token']
                access_token = json.loads(resp.data.decode())['access_token']
                rt = self.client.post('/api/v1/meetups/create', headers=dict(Authorization=admin_header),data=json.dumps(self.meetup_data_no),content_type='application/json')
                response = self.client.post('api/v1/meetups/3/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status_no),content_type='application/json')
                result = json.loads(response.data.decode())
                self.assertTrue(result['status'] == 200)
                self.assertTrue(result['message'] == 'Meetup is not reserved.')
                self.assertEqual(response.status_code, 200)

    def test_admin_can_not_rsvpt(self):
        with self.client:
            """
            Test status no does not reserve meetup
            """
            resp = self.login_user_admin()
            access_token = json.loads(resp.data.decode())['access_token']
            rt = self.client.post('/api/v1/meetups/create', headers=dict(Authorization=access_token),data=json.dumps(self.meetup_data_no),content_type='application/json')
            response = self.client.post('api/v1/meetups/4/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status),content_type='application/json')
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 401)
            self.assertTrue(result['message'] == 'Admin cannot reserve a meetup')
            self.assertEqual(response.status_code, 401)


    def test_blank_status(self):
        with self.client:
            """
            Test status no does not reserve meetup
            """
            resp = self.login_user()
            admin_login= self.login_user_admin()
            admin_header = json.loads(admin_login.data.decode())['access_token']
            access_token = json.loads(resp.data.decode())['access_token']
            rt = self.client.post('/api/v1/meetups/create', headers=dict(Authorization=admin_header),data=json.dumps(self.meetup_data_no),content_type='application/json')
            response = self.client.post('api/v1/meetups/3/rsvp', headers=dict(Authorization=access_token),data=json.dumps(self.status_nill),content_type='application/json')
            result = json.loads(response.data.decode())
            print(result)
            self.assertTrue(result['status'] == 400)
            self.assertTrue(result['message'] == 'Provide a status (yes, no, or maybe).')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
                