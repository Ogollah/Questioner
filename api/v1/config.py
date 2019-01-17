"""
This file holds configuration environment for the api.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration:
    """
    Base configuration
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'this_is_very_secret')
    DEBUG = False
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET_KEY = 'no-need-to-ask-it-is-a-secret'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CKECKS = ['access','refresh']

class DevelopmentConfig(Configuration):
    """
    Development configuration
    """
    DEBUG = True
    ERROR_404_HELP = False

class TestingConfig(Configuration):
    """
    Testing configuration
    """
    DEBUG = True
    TESTING = True

class ProductionConfig(Configuration):
    """Production configuration
    """
    DEBUG = False

# configurations
api_congig = dict(
    development=DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
