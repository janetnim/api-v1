from flask import Flask, request, jsonify
from flask_restful import  Api
from config import config
from views.models import User_login, User_SignUp
from views.models import Request
# from test.test_api import TestModels


app = Flask(__name__)
api = Api(app)


api.add_resource(User_SignUp, '/auth/signup', methods=['POST'])
api.add_resource(User_login, '/auth/login', methods=['POST'])
# api.add_resource(Request, '/users/requests', methods=['POST'])
# api.add_resource(Request, '/users/requests', methods=['GET'])
# api.add_resource(Request, '/users/requests/<int:request_id>', methods=['GET'])
# api.add_resource(Request, '/users/requests/<int:request_id>', methods=['PUT'])
# api.add_resource(Request, '/users/requests/<int:request_id>', methods=['DELETE'])
# api.add_resource(Request, '/requests', methods=['GET'])
# api.add_resource(Request, 'requests/<int:request_id>/approve', methods=['PUT'])
# api.add_resource(Request, 'requests/<int:request_id>/disapprove', methods=['PUT'])
# api.add_resource(Request, 'requests/<int:request_id>/resolve', methods=['PUT'])
# api.add_resource(Request, 'requests/<int:request_id>/delete', methods=['DELETE'])


if __name__ == '__main__':
	app.run(debug=True)
