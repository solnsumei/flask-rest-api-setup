import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt import JWT
from src.utils.security import authenticate, identity
from src.models.basemodel import db


def initdb(flask_app):
    db.init_app(flask_app)


def create_app():
    from src.routes.api import routes, admin_routes

    flask_app = Flask(__name__)
    flask_app.config.from_pyfile('config.py')

    bp = Blueprint('api', __name__, static_url_path="assets")

    admin_bp = Blueprint('admin', __name__, static_url_path="assets")

    api = Api(bp)
    admin = Api(admin_bp)

    routes(api)
    admin_routes(admin)

    flask_app.register_blueprint(bp, url_prefix="/api/v1")

    flask_app.register_blueprint(admin_bp, url_prefix="/api/v1/admin")

    JWT(flask_app, authenticate, identity)  # /auth

    @flask_app.route('/')
    def index():
        return 'Welcome to Flask Rest API Setup!'

    initdb(flask_app)

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run()
