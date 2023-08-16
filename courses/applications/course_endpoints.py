from config import api
from flask_restx import Resource
from config.token_required import token_required
from .dtos.course_dto import course_request
from ..models.course_models import Course
from .course_services import CourseService

ns = api.namespace('default', description='default namespace')


@ns.route('/course')
class CourseEndpoints(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.service = CourseService()
        super().__init__(api, *args, **kwargs)

    @ns.doc('list_all')
    def get(self):
        return {}

    @ns.doc('create courses')
    @ns.expect(course_request)
    @token_required
    def post(self):
        try:
            course_dto = api.payload
            course = Course(course_dto['title'], course_dto['description'])
            self.service.create_course(course)
            return 200
        except Exception as e:
            return 400
