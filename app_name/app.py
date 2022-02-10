from flask import Flask
from flask_cors import CORS
from app_name.api import blueprintAPI
from app_name.extensions import db


def initialize_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("app_name")
    CORS(app)

    app.config.from_object("app_name.settings")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)

    register_blueprints(app)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)


def register_blueprints(app):
    """register all name space for application"""
    app.register_blueprint(blueprintAPI)
