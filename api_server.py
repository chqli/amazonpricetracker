import uuid

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Register(Resource):

    def post(self):
        return {'id': uuid.uuid4().int >> 64}


class Data(Resource):
    def get(self, todo_id):
        if int(todo_id) % 2 == 0:
            return {'sold': True}
        return {'sold': False}


api.add_resource(Register, '/register-request')
api.add_resource(Data, '/request-data/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
