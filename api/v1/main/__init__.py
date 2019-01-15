"""
This file initialize the project.
"""

from flask import Flask
from flask_jwt_extended import JWTManager

# local import
from api.v1.config import api_congig
from api.v1.main.service.user_auth_service import blacklist

def creat_app(config_name):
    api = Flask(__name__)
    api.config.from_object(api_congig[config_name])
    jwt = JWTManager(api)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    return api
