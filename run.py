from flask import Flask, request, jsonify
from flask_restful import  Api, Resource
from flask_jwt_extended import JWTManager
from helper import helper
from views import models
from flask_cors import CORS

database = {
	"DEVELOPMENT": {
		"DATABASE_NAME": "maintenance",
		"DATABASE_PASSWORD": "123456",
		"DATABASE_USER": "janet",
		"DATABASE_HOST": "localhost"
	},
	"TESTING": {
		"DATABASE_NAME": "maintenance_test",
		"DATABASE_PASSWORD": "123456",
		"DATABASE_USER": "janet",
		"DATABASE_HOST": "localhost"
	},
	"PRODUCTION":{
		"DATABASE_NAME": "ddecsfpmjv8jf",
		"DATABASE_PASSWORD": "fcfa39797020dcd64b88152cea3be28c4c90cc8e56a4dd9bd851f93d310b2f96",
		"DATABASE_USER": "ogtczsiotxgjvs",
		"DATABASE_HOST": "ec2-50-16-241-91.compute-1.amazonaws.com"
	},
}
 
def create_app(environment = "DEVELOPMENT"):
	app = Flask(__name__, instance_relative_config=True)
	CORS(app)
	api = Api(app)
	
	app.config['DATABASE_NAME'] = database[environment]['DATABASE_NAME']
	app.config['DATABASE_PASSWORD'] = database[environment]['DATABASE_PASSWORD']
	app.config['DATABASE_USER'] = database[environment]['DATABASE_USER']
	app.config['DATABASE_HOST'] = database[environment]['DATABASE_HOST']

	helper.initialize(app)

	app.config['JWT_SECRET_KEY'] = "my awesome secret key"

	jwt = JWTManager(app)

	api.add_resource(models.User_SignUp, '/api/v2/auth/signup', methods=['POST'])
	api.add_resource(models.User_login, '/api/v2/auth/login', methods=['POST'])
	api.add_resource(models.MakeRequest, '/api/v2/users/requests', methods=['POST'])
	api.add_resource(models.ViewAllRequest, '/api/v2/users/requests', methods=['GET'])
	api.add_resource(models.RequestView, '/api/v2/users/requests/<int:request_id>', methods=['GET'])
	api.add_resource(models.ModifyRequest, '/api/v2/users/requests/<int:request_id>', methods=['PUT'])
	api.add_resource(models.DeleteRequest, '/api/v2/users/requests/<int:request_id>', methods=['DELETE'])
	api.add_resource(models.AdminGetRequest, '/api/v2/requests', methods=['GET'])
	api.add_resource(models.AdminGetOneRequest,"/api/v2/requests/<int:request_id>", methods=['GET'])
	api.add_resource(models.ApproveRequest, '/api/v2/requests/<int:request_id>/approve', methods=['PUT'])
	api.add_resource(models.DisapproveRequest, '/api/v2/requests/<int:request_id>/disapprove', methods=['PUT'])
	api.add_resource(models.AdminResolveRequest, '/api/v2/requests/<int:request_id>/resolve', methods=['PUT'])
	api.add_resource(models.AdminDeleteRequest, '/api/v2/requests/<int:request_id>/delete', methods=['DELETE'])
	
	return app

app = create_app("PRODUCTION")

if __name__ == '__main__':
	app.run(debug=True)