"""
This file tests user signup testcases.
"""

import unittest 
import json
import datetime

# local imports
from api.v1.main.model.user import User, USERS
from api.v1.test.base_test import BaseTestCase


# create normal user 
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

# create normal user 
def signup_user_dub(self):
    return self.client.post(
        '/api/v1/user/signup',
            data=json.dumps(dict(
            firstname='Jhone',
            lastname='Doe',
            othername='Johnson',
            phoneNumber='+25422034587',
            email='duplicate@mail.com',
            username='example',
            password='42qwR@#'
        )),
        content_type='application/json'
    )


# create invalid email
def user_data_invalid_email(self):
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

# create invalid min number of password
def user_data_invalid_min_pass(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='Johnson',
    phoneNumber='+25422034587',
    email='min@mail.com',
    username='example',
    password='4wW@'
    )),
    content_type='application/json'
)

# create invalid max number of password
def user_data_invalid_max_pass(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='Johnson',
    phoneNumber='+25422034587',
    email='max@mail.com',
    username='example',
    password='4wW@ujkkjkksgfattutuytytyfgf' 
    )),
    content_type='application/json'
)



# create invalid upper case password
def user_data_invalid_upper_case(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='Johnson',
    phoneNumber='+25422034587',
    email='upper@mail.com',
    username='example',
    password='@2wrong'    
    )),
    content_type='application/json'
)



# create invalid lower case password
def user_data_invalid_lower_case(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='Johnson',
    phoneNumber='+25422034587',
    email='lower@mail.com',
    username='example',
    password='4KKKKKKKKW@'   
    )),
    content_type='application/json'
)



# create invalid special password
def user_data_invalid_special(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='Johnson',
    phoneNumber='+25422034587',
    email='special@mail.com',
    username='example',
    password='wWrong'  
    )),
    content_type='application/json'
)



# create invalid number case password
def user_data_invalid_number(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='Johnson',
    phoneNumber='+25422034587',
    email='number@mail.com',
    username='example',
    password='wWrong@'  
        )),
    content_type='application/json'
)



# create invalid username length
def user_data_invalid_username(self):
    return self.client.post(
    '/api/v1/user/signup',
        data=json.dumps(dict(
    firstname='Jhone',
    lastname='Doe',
    othername='John',
    phoneNumber='+25422034587',
    email='username@mail.com',
    username='exa',
    password='Pass@2'   
    )),
    content_type='application/json'
)


class TestUserSignup(BaseTestCase):

    def test_succesful_user_signup(self):
        with self.client:
            """
            Test succesful signup.
            """
            response = signup_user(self)
            # return result in json format
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 201)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_duplicate_signup(self):
        """
        Test user signup already signup user.
        """
        
        with self.client:
            signup_user_dub(self)
            response = signup_user_dub(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 409)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_valid_email(self):
        """
        Test for email validity
        """
        with self.client:
                                    
            response = user_data_invalid_email(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_max_password_length(self):
        """
        Password length.
        """

        with self.client:
                                    
            response = user_data_invalid_max_pass(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_min_password_length(self):
        """
        Password length.
        """

        with self.client:
                                   
            response = user_data_invalid_min_pass(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_special_character_password(self):
        """
        Password with no special character.
        """

        with self.client:
                                   
            response = user_data_invalid_special(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_lower_password(self):
        """
        Password with no lowercase character.
        """

        with self.client:
                                   
            response = user_data_invalid_lower_case(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_caps_password(self):
        """
        Password with no capital character.
        """

        with self.client:
                                   
            response = user_data_invalid_upper_case(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_no_numb_password(self):
        """
        Password with no numeric value.
        """

        with self.client:
                                   
            response =user_data_invalid_number(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    
    def test_username_length(self):
        """
        Username length
        """

        with self.client:
                                   
            response = user_data_invalid_username(self)
            result = json.loads(response.data.decode())
            self.assertTrue(result['status'] == 400)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
    