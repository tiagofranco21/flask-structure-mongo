from functools import wraps
from flask import request

def access_required(allowed_roles=[], allowed_role=""):
    
    if len(allowed_roles) > 0 and allowed_role != "":
        allowed_roles = [allowed_role]
        
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
                
                
                token_info = _decode_token(token)

                role = token_info["role"]

                if len(allowed_roles) > 0 and role not in allowed_roles:
                    return {'message': "User does not have access"}, 401
                
                
            except Exception as error:
                return {'message': str(error)}, 401

            return func(self, *args, **kwargs)

        return decorated
    return token_required


def _decode_token(token):
    
    # decode the token and extract the payload info 
    example_info = {"role": "master", "name": "Tiago Franco"}
    
    return example_info