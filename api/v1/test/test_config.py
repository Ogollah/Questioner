"""
This file holds testcases for api configuration.
"""

import os
import unittest

from flask import current_app
from flask_testing import TestCase

# local imports
from manage import api
from api.v1.config import basedir

class TestDevelopmentConfiguration(TestCase):
    """
    Testing development configuration.
    """
    def create_app(self):
        api.config.from_object('api.v1.config.DevelopmentConfig')
        return api

    # test api in development environment
    def test_api_development_env(self):
        self.assertTrue(api.config['DEBUG'] is True)

class TestTestingConfig(TestCase):
    """
    Testing testing configuration
    """
    def create_app(self):
        api.config.from_object('api.v1.config.TestingConfig')
        return api

    # test api in testing environment
    def test_api_testing_env(self):
        self.assertTrue(api.config['DEBUG'] is True)
        self.assertTrue(api.config['TESTING'] is True)

class TestProductionConfig(TestCase):
    """
    Testing production configuration
    """
    def create_app(self):
        api.config.from_object('api.v1.config.ProductionConfig')
        return api

    # test api in production environment
    def test_api_production_env(self):
        self.assertTrue(api.config['DEBUG'] is False)

if __name__ == '__main__':
    unittest.main()
