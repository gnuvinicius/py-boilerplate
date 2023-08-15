from flask import Flask
from config import api
from courses.course_endpoints import ns


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    api.add_namespace(ns)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
