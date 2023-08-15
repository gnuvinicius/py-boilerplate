from flask import Blueprint, Response
from flask_restx import Api
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from courses.course_models import Base
from asyncio import run


''' stating database config '''

url_sqlite3_async = 'sqlite+aiosqlite:///db.sqlite3'

engine = create_async_engine(url_sqlite3_async)

session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

run(create_database())


''' end database config '''


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
