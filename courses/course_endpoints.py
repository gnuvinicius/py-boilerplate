from config import api
from flask_restx import Resource
from .dtos.course_dto import course_request
from flask import request, jsonify
from asyncio import run
import hashlib

from .course_models import Course
from .course_repository import CourseRepository

ns = api.namespace('default', description='default namespace')


@ns.route('/course')
class CourseEndpoints(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.repository = CourseRepository()
        super().__init__(api, *args, **kwargs)

    @ns.doc('list_all')
    def get(self):
        return {}

    @ns.doc('create courses')
    @ns.expect(course_request)
    def post(self):
        encoded = 'integration-system-password'.encode()
        encrypted = hashlib.sha256(encoded)

        course_dto = api.payload

        run(self.repository.create_course(course=Course(
            course_dto['title'], course_dto['description'])))

        return {'hello': encrypted.hexdigest()}
