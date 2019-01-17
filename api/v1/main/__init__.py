"""
This file initialize the project.
"""

from flask import Flask
from flask_jwt_extended import JWTManager
import datetime

# local import
from api.v1.config import api_congig
from api.v1.main.service.user_auth_service import blacklist
from api.v1.main.model.user import User, USERS
from api.v1.main.model.question import Question, QUESTIONS
from api.v1.main.model.meetup import Meetup, MEETUPS

def creat_app(config_name):
    api = Flask(__name__)
    api.config.from_object(api_congig[config_name])
    jwt = JWTManager(api)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    def is_admin():
        user = User()
        user.firstname = "Hezzy"
        user.lastname = "Marimu"
        user.othername = "John"
        user.phoneNumber = "+25723456712"
        user.email = "example@admin.com"
        user.set_password_hash("@Aadm@3In")
        user.username = "useradmin2"
        user.registered =datetime.datetime.now()
        user.isAdmin=True
        USERS.append(user)

    def meetup():
        date = '2018-06-29 08:15'
        meetup = Meetup()
        meetup.description = "Just another meetup"
        meetup.happeningOn = str(datetime.datetime.strptime(date, '%Y-%m-%d %H:%M'))
        meetup.host = "mwaura"
        meetup.hostFrom = "Kenya"
        meetup.images = "image"
        meetup.Tags ="tags"
        meetup.topic ="Nice topic"
        MEETUPS.append(meetup)


    is_admin()
    meetup()
    return api
