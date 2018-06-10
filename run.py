from flask import Flask, request, jsonify
from flask_restful import  Api, Resource
from config import config
from flask_jwt_extended import JWTManager
from helper import Database

helper = Database()

import models

database = {
	"DEVELOPMENT": "maintenance",
	"TESTING": "maintenance_test"
}


def create_app(environment = "DEVELOPMENT"):
	app = Flask(__name__)
	api = Api(app)
	
	app.config['DATABASE_NAME'] = database[environment]

	helper.initialize(app)

	app.config['JWT_SECRET_KEY'] = "my awesome secret key"

	jwt = JWTManager(app)


	# api.add_resource(models.User_SignUp, '/auth/signup', methods=['POST'])
	api.add_resource(models.User_login, '/auth/login', methods=['POST'])
	api.add_resource(models.MakeRequest, '/users/requests', methods=['POST'])
	api.add_resource(models.ViewAllRequest, '/users/requests', methods=['GET'])
	api.add_resource(models.RequestView, '/users/requests/<int:request_id>', methods=['GET'])
	api.add_resource(models.ModifyRequest, '/users/requests/<int:request_id>', methods=['PUT'])
	api.add_resource(models.DeleteRequest, '/users/requests/<int:request_id>', methods=['DELETE'])
	api.add_resource(models.AdminGetRequest, '/requests', methods=['GET'])
	api.add_resource(models.ApproveRequest, '/requests/<int:request_id>/approve', methods=['PUT'])
	api.add_resource(models.DisapproveRequest, '/requests/<int:request_id>/disapprove', methods=['PUT'])
	api.add_resource(models.AdminResolveRequest, '/requests/<int:request_id>/resolve', methods=['PUT'])
	api.add_resource(models.AdminDeleteRequest, '/requests/<int:request_id>/delete', methods=['DELETE'])
	
	return app

app = create_app()

if __name__ == '__main__':
	app.run(debug=True, host="192.168.0.194")
