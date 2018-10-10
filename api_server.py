import uuid

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Register(Resource):

    def post(self):
        return {'id': uuid.uuid4().int >> 64}


class Sold(Resource):
    def get(self, register_id):
        if int(register_id) % 2 == 0:
            return {'sold': True}
        return {'sold': False}


api.add_resource(Register, '/register-request')
api.add_resource(Sold, '/request-data/<int:register_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
