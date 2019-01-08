"""
This file marshall data for api calls.
"""

from flask_restplus import Namespace, fields

class UserDto:
    # create name space for user operations
    api = Namespace('User', description='User opertaions')
    user = api.model('user',{
        'id' : fields.Integer(description='User Identification'),
        'firstname': fields.String(required=True, description='User first name'),
        'lastname': fields.String(required=True, description='User last name'),
        'othername': fields.String(required=True, description='User other name'),
        'email': fields.String(required=True, description='User email'),
        'phoneNumber': fields.String(required=True, description='User phone number'),
        'username': fields.String(required=True, description='User username'),
        'registered' : fields.String(description='User regitered date'),
        'isAdmin' : fields.Boolean(description='User role')
    })
