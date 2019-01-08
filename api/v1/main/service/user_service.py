"""
This file contains logic for user model.
"""

import datetime
import re

# local imports
from api.v1.main.model.user import User, USERS

def get_user_by_email(email):
    """
    Get user by user email 
    """
    for user in USERS:
        if user == email:
            return user

# save a user details
def save_user_details(user_data):
    USERS.append(user_data)

# save new user
def save_new_user(user_data):

    firstname = user_data["firstname"]
    lastname = user_data["lastname"]
    othername = user_data["othername"]
    phoneNumber = user_data["phoneNumber"]
    email = re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user_data['email'])
    password_hash = validate_password(password=user_data['password'])
    username = user_data['username']
    registered =datetime.datetime.utcnow()
    user = get_user_by_email(email=user_data['email']) 

    if user:
        response_object = {
            'status':'fail',
            'message':'User with this email address already exist.'
        }
        return response_object, 409

    if not username:
        response_object = {
            'status':'fail',
            'message':'Username not be less than 4 characters.'
        }
        return response_object, 400

    if not email:
        response_object = {
            'status':'fail',
            'message':'Check format of your email.'
        }
        return response_object, 400

    if not password_hash:
        if not check_pass_min_length(password=user_data['password']):
            response_object = {
            'status':'fail',
            'message':'Password should not be less than 6 characters.'
             }
            return response_object, 400

        if not check_pass_max_length(password=user_data['password']):
            response_object = {
            'status':'fail',
            'message':'Password should not be more than 16 characters.'
             }
            return response_object, 400

        if not check_lower_case(password=user_data['password']):
            response_object = {
            'status':'fail',
            'message':'Password should contain a lower case character'
        }
            return response_object, 400

        if not check_numb(password =user_data['password']):
            response_object = {
            'status':'fail',
            'message':'Password should contain atleast one number/ integer.'
        }
            return response_object, 400
    
        if not check_special_character(password=user_data['password']):
            response_object = {
            'status':'fail',
            'message':'Password should contain a special character.'
             }
            return response_object, 400
        if not check_upper_case(password=user_data['password']):
            response_object = {
            'status':'fail',
            'message':'Password should contain a capital letter'
             }
            return response_object, 400

    if password_hash and email and not user:
        
        new_user = User(firstname, lastname, othername, phoneNumber, username, registered, password_hash,email)

        print(password_hash)
        save_user_details(new_user)
        response_object = {
            'status': 'success',
            'message':'You have signed up successfully.'
        }
        return response_object, 201 

# username length
def check_username_length(username):
    valid = len(username) <=4
    return valid

#check for upper case 
def check_upper_case(password):
    valid = (any(char.isupper() for char in password))
    return valid
#check for digit 
def check_numb(password):
    valid = (any(char.isdigit() for char in password))
    return valid

#check password minimum password length
def check_pass_min_length(password):
    valid = len(password) >=6 
    return valid

#check password max length
def check_pass_max_length(password):
    valid = len(password) <=12
    return valid

#check for special character in the string
def check_special_character(password):
    #regular expression matching
    valid = re.search("[@_!#$%^&*()<>?/\|}{~:]",password) 
    return valid
#check for lower case character in a string
def check_lower_case(password):
    valid = (any(char.islower() for char in password))
    return valid
#validating password    
def validate_password(password):
    if check_special_character(password) and check_lower_case(password) and check_numb(password) and check_pass_min_length(password) and check_pass_max_length(password) and check_upper_case(password):
        return password
