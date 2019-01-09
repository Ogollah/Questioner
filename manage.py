"""
This file is the entry point of the api.
"""

import os
import unittest

from flask_script import Manager

# local imports
from api.v1.main import creat_app
from api import blueprint

# call create app
api = creat_app(os.getenv('QUESTIONER_ENV') or 'development')
api.register_blueprint(blueprint)
api.app_context().push()

manager = Manager(api)

@manager.command
def run():
    """
    Run the api application on the local development server.
    """
    api.run()

@manager.command
def test():
    """
    Runs the api tests
    """
    tests = unittest.TestLoader().discover('api/v1/test', pattern='test*.py')
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)
    if test_result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
    