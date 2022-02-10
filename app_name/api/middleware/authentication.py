from functools import wraps
from flask import request


def token_required(func):
    @wraps(func)
    def decorated(self, *args, **kwargs):

        token = None
        prefix = 'Bearer '

        if 'Authorization' in request.headers:
            if not request.headers['Authorization'].startswith(prefix):
                return {'message': 'Token is missing.'}, 401

            token = request.headers['Authorization'][len(prefix):]

        if not token:
            return {'message': 'Token is missing.'}, 401

        try:
            # validate your token here
            if token != "1":
                return {'message': "Token invalid"}, 401
        except Exception as error:
            return {'message': str(error)}, 401

        return func(self, *args, **kwargs)

    return decorated
