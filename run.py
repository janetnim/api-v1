from flask import Flask, request, jsonify
from flask_restful import  Api, Resource
from config import config
from flask_jwt_extended import JWTManager
import manage
from models import User_login, User_SignUp, MakeRequest, ViewAllRequest, RequestView, ModifyRequest, DeleteRequest, AdminGetRequest, ApproveRequest, DisapproveRequest,AdminResolveRequest, AdminDeleteRequest
# from test.test_api import TestModels


app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = "my awesome secret key"

jwt = JWTManager(app)


api.add_resource(User_SignUp, '/auth/signup', methods=['POST'])
api.add_resource(User_login, '/auth/login', methods=['POST'])
api.add_resource(MakeRequest, '/users/requests', methods=['POST'])
api.add_resource(ViewAllRequest, '/users/requests', methods=['GET'])
api.add_resource(RequestView, '/users/requests/<int:request_id>', methods=['GET'])
api.add_resource(ModifyRequest, '/users/requests/<int:request_id>', methods=['PUT'])
api.add_resource(DeleteRequest, '/users/requests/<int:request_id>', methods=['DELETE'])
api.add_resource(AdminGetRequest, '/requests', methods=['GET'])
api.add_resource(ApproveRequest, '/requests/<int:request_id>/approve', methods=['PUT'])
api.add_resource(DisapproveRequest, '/requests/<int:request_id>/disapprove', methods=['PUT'])
api.add_resource(AdminResolveRequest, '/requests/<int:request_id>/resolve', methods=['PUT'])
api.add_resource(AdminDeleteRequest, '/requests/<int:request_id>/delete', methods=['DELETE'])


if __name__ == '__main__':
	app.run(debug=True)
