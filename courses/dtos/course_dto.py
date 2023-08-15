from config import api
from flask_restx import fields

student_request = api.model('Student', {
    'id': fields.String(readonly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details'),

})

course_request = api.model('Course', {
    'id': fields.String(readonly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The task details'),
    'description': fields.String(required=True, description='The task details'),
    'students': fields.List(fields.Nested(student_request))
})
