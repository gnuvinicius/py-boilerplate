from app.extensions import api
from flask_restx import Resource
import hashlib

ns = api.namespace('default', description='default namespace')


@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        encoded = 'integration-system-password'.encode()
        encrypted = hashlib.sha256(encoded)

        return {'hello': encrypted.hexdigest()}
