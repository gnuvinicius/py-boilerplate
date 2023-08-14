from flask import Flask
from .config import api, engine
from .courses.course_endpoints import ns


def create_app():
    app = Flask(__name__)

    api.init_app(app)
    # db.init_app(app)

    api.add_namespace(ns)

    return app
