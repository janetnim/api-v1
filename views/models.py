from flask_restful import Resource, reqparse
from  flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from flask import jsonify
import psycopg2
from  helper import helper
import re
from functools import wraps
from passlib.handlers.bcrypt import bcrypt


def role_admin_required(f):
	@wraps(f)
	def wrapped(*args, **kwargs):
		user = User_login().get_one_user(get_jwt_identity())
		if user['role'] != 'admin':
			return {"message": "You are not an admin"}, 401
		return f(*args, **kwargs)
	return wrapped

class Get_All_Users(Resource):
	def get(self):
		users = helper.get_users()
		return {'users': users}

class User_SignUp(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, help='invalid username')
		parser.add_argument('email', type=str, help='Please enter email')
		parser.add_argument('password', type=str, help='Please enter password')
		args = parser.parse_args()

		username = args['username']
		email = args['email']
		password = args['password']

		if username == "" or email == "" or password == "":
			return {"message": "Please enter all details"}
		elif username == " " or email == " " or password == " ":
			return {"message": "Invalid entry try again"}
		elif re.match(r'^.+@([?)[a-zA-Z0-9-.])+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$' , email) is None:
			return {"message": "invalid email"}, 400
		elif re.match(r'^[0-9]+$', username) is not None:
			return {"message": "invalid username"}, 400
		elif not isinstance(username, str) or not isinstance(password, str):
			return {"message": "Enter a string value for username and password"}
		res = helper.get_user_by_username(username)
		if res is not None:
			return {"message": "The user already exists"}, 202
		helper.add_user(username, bcrypt.encrypt(password), email)
		helper.get_user_by_username(username)
		return {"message": "User successfully signed up"}, 201
	

class User_login(Resource):
	def get_one_user(self, username):
		user = helper.get_user_by_username(username)
		return user

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, help='invalid username')
		parser.add_argument('password', type=str, help='invalid password')
		args = parser.parse_args()

		username = args['username']
		password = args['password']

		hash = bcrypt.encrypt(password)

		user = User_login().get_one_user(username)
		if user is None or len(user)==0:
			return {"message":"user not found"}, 404
		elif user['username'] != username:
			return {"message":"incorrect username"}
		if not bcrypt.verify(password,user['password']):
			return {"message":"incorrect password"}
		elif re.match(r'^[0-9]+$', username) is not None:
			return {"message": "invalid username"}, 400
		if not isinstance(username, str) or not isinstance(password, str):
			return {"message": "Enter a string value for username and password"}
		if username=="" or password=="":
			return {"message":"Enter all details"}
		if len(username.split()) == 0 or len(password.split())==0:
			return {"message": "Invalid entry try again"}
		role = helper.get_role(username)
		username = helper.get_user(username)
		token = create_access_token(identity=username)
		return {"message": "You have logged in successfully", "token":token, "role":role, "username":username}


class MakeRequest(Resource):
	@jwt_required
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('request', type=str, help='invalid request')
		parser.add_argument('department', type=str, help='invalid department')
		parser.add_argument('status', type=str, help='invalid status')
		args = parser.parse_args()

		request = args['request']
		department = args['department']
		status = args['status']
		user = User_login().get_one_user(get_jwt_identity())

		if request =="" or department=="":
			return {"message": "Please fill all details"}
		elif len(request.split()) == 0 or len(department.split())==0:
			return {"message": "Invalid entry try again"}
		elif not isinstance(request, str) or not isinstance(department, str):
			return {"message": "Enter a string value for request and department"}
		request_id = helper.insert_user_request(request, department, user['personal_id'])
		return {"message":"request made successfully", "request_id": request_id} , 201


class RequestView(Resource):
	@jwt_required
	def get(self, request_id):
		user = User_login().get_one_user(get_jwt_identity())
		res = helper.get_user_request(request_id, user['personal_id'])
		if res is None or len(res) == 0:
			return {"message":"Request not found"}, 404
		return {"res":res}


class ModifyRequest(Resource):
	@jwt_required
	def put(self, request_id):
		parser = reqparse.RequestParser()
		parser.add_argument('request', type=str, help='invalid request')
		args = parser.parse_args()

		req = args['request']

		user = User_login().get_one_user(get_jwt_identity())

		res = helper.get_user_request(request_id, user['personal_id'])
		if res is None or len(res) == 0:
			return {"message": "Request does not exist"}
		if res['status'] == "Pending":
			helper.modify_user_request(request_id, req)
		else:
			return {"message": "Only a pending request can be modified."}, 400
		res = helper.get_user_request(request_id, user['personal_id'])
		return {"request" : res}


class DeleteRequest(Resource):
	@jwt_required
	def delete(self, request_id):
		user = User_login().get_one_user(get_jwt_identity())
		res = helper.get_user_request(request_id, user['personal_id'])
		if res is None or len(res) == 0:
			return {"message":"Request does not exist!"}
		helper.delete_request_by_id(request_id)
		helper.admin_get_all_requests()
		return {"message":"Deleted successfully"}, 200


class ViewAllRequest(Resource):
	@jwt_required
	def get(self):
		user = User_login().get_one_user(get_jwt_identity())
		res = helper.user_get_all(user['personal_id'])
		if res is None or len(res) == 0:
			return {"message": "No requests available"}
		return {"res":res}

	'''Admin endpoints'''
class AdminGetRequest(Resource):
	@jwt_required
	@role_admin_required
	def get(self):
		res = helper.admin_get_all_requests()
		if res is None or len(res) == 0:
			return {"message": "No requests available"}
		return {"Request":res}

class AdminApproveRequest(Resource):
	@jwt_required
	@role_admin_required
	def get(self):
		res = helper.admin_get_approved_requests()
		if res is None or len(res) == 0:
			return {"message": "No requests available"}
		return {"Request":res}

class AdminRejectRequest(Resource):
	@jwt_required
	@role_admin_required
	def get(self):
		res = helper.admin_get_rejected_requests()
		if res is None or len(res) == 0:
			return {"message": "No requests available"}
		return {"Request":res}

class AdminResolveRequests(Resource):
	@jwt_required
	@role_admin_required
	def get(self):
		res = helper.admin_get_resolved_requests()
		if res is None or len(res) == 0:
			return {"message": "No requests available"}
		return {"Request":res}

class ApproveRequest(Resource):
	@jwt_required
	@role_admin_required		
	def put(self, request_id):
		res = helper.get_request_by_id(request_id)
		if res is None:
			return {"message":"Request does not exist"}
		helper.approve_request_by_id(request_id)
		return {"Request":res}

class AdminGetOneRequest(Resource):
	@jwt_required
	@role_admin_required
	def get(self, request_id):
		res = helper.get_request_by_id(request_id)
		if res is None:
			return {"message":"Request does not exist"}
		return {"Request":res}

class DisapproveRequest(Resource):
	@jwt_required
	@role_admin_required
	def put(self, request_id):
		res = helper.get_request_by_id(request_id)
		if res is None:
			return {"message":"Request does not exist"}
		helper.disapprove_request_by_id(request_id)
		return {"Request":res}

class AdminResolveRequest(Resource):
	@jwt_required
	@role_admin_required
	def put(self, request_id):
		res = helper.get_request_by_id(request_id)
		if res is None:
			return {"message":"Request does not exist"}
		helper.resolve_request_by_id(request_id)
		return {"Request":res}

class AdminDeleteRequest(Resource):
	@jwt_required
	@role_admin_required
	def delete(self, request_id):
		res = helper.get_request_by_id(request_id)
		if res is None or len(res) == 0:
			return {"message": "Request does not exist!"}
		helper.delete_request_by_id(request_id)
		helper.admin_get_all_requests()
		return {"message":"Deleted successfully"}, 200
