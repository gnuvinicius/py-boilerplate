from app.config import api
from flask_restx import Resource
from asyncio import run
import hashlib

from .course_models import Course
from .course_repository import CourseRepository

ns = api.namespace('default', description='default namespace')


@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        encoded = 'integration-system-password'.encode()
        encrypted = hashlib.sha256(encoded)

        repository = CourseRepository()

        run(repository.create_course(course=Course(
            'title1', 'description for title1')))

        return {'hello': encrypted.hexdigest()}
