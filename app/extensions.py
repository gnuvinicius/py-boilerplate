from flask import Blueprint
from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

blueprint = Blueprint('api', __name__)

api = Api(version='1.0', title='Garage 474 Api',
          description='description of garage api')


@api.errorhandler
def default_error_handle(e):
    message = 'An unhandled exception occurred.'

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return {'message': 'A database result was required but none was found.'}, 404
