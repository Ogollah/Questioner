"""
This file holds meetups test cases.
"""

import unittest
import json

# local imports
from api.v1.test.base_test import BaseTestCase

class MeetupsTestCases(BaseTestCase):
    def test_successful_get_all_meetups(self):
        with self.client:
            """
            Test succesfuly get a list of all meetups
            """
            # signup user
            self.signup_user()
            # signin user
            self.signin_user
            response = self.get_all_meetups_available()
            self.assertEqual(response.status_code, 200)
