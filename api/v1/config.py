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

class DevelopmentConfig(Configuration):
    """
    Development configuration
    """

class TestingConfig(Configuration):
    """
    Testing configuration
    """

class ProductionConfig(Configuration):
    """Production configuration
    """

# configurations
api_congig = dict(
    development=DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
