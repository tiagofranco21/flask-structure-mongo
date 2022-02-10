from flask import Blueprint
from app_name.api.restplus import api
from app_name.api.resources import books_namespace

blueprintAPI = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprintAPI)
api.add_namespace(books_namespace)

__all__ = ["blueprintAPI"]
