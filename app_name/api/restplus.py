from flask import current_app as app
from flask_restx import Api
from app_name.extensions import log

authorizations = {
    'Authorization': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


api = Api(version='1.0', title='Flask API - Repository structure with Mongoengine',
          description="Sample repository structure", authorizations=authorizations)


@api.errorhandler
def default_error_handler(error):
    """
    Default error handler method

    :param error: error message
    :return: Message Error response
    """
    message = 'An unhandled exception occurred.'
    log.exception(message)
    log.exception(error)
    if not app.confg["FLASK_DEBUG"]:
        return {'message': message}, 500
    return error
