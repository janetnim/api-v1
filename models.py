from flask_restful import Resource, reqparse
from  flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from flask import jsonify
from manage import create_tables,cur,conn
import psycopg2
import helper
# from werkzeug.security import generate_password_hash, \
#      check_password_hash

create_tables()
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
			return "Please enter all details"
		if username == " " or email == " " or password == " ":
			return "Invalid entry try again"
		if not isinstance(username, str)or not isinstance(email, str) or not isinstance(password, int):
			return jsonify({"message": "Enter a string value for username, email and password"})
		res = helper.get_users_by_username()
		if res is not None and username in res:
			return "The user already exists"
		helper.add_user(username,password, email)
		helper.get_user_by_username(username)
		return "User successfully signed up"


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

		helper.get_user_by_username_and_password(username, password)
		user = User_login().get_one_user(username)
		if user is None or len(user)==0:
			return jsonify({"message":"user not found"}), 404
		elif user['password'] != password:
			return jsonify({"message":"incorrect password"})
		else:
			token = create_access_token(identity=username)
			return jsonify({"message": "logged in successfully", "token":token})
		return make_response("cannot verify", 401, {"WWW-Authentication": "Basic realm='Login required'"})

		if username=="" or password=="":
			return jsonify({"message":"Enter all details"})
		if len(username.split()) == 0 or len(password.split())==0:
			return jsoniffy({"message": "Invalid entry try again"})
		helper.get_users_by_username()
		if not isinstance(username, str) or not isinstance(password, str):
			return jsonify({"message": "Enter a string value for username and password"})
		if username not in res:
			return jsonify({"message":"You are not a user"})
		return jsonify({"message":"you have logged in successfully"})


class MakeRequest(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('request', type=str, help='invalid request')
		parser.add_argument('department', type=str, help='invalid department')
		parser.add_argument('status', type=str, help='invalid status')
		args = parser.parse_args()

		request = args['request']
		department = args['department']
		status = args['status']

		if request=="" or department=="":
			return jsonify({"message": "Please fill all details"})
		if not isinstance(request, str) or not isinstance(department, str):
			return jsonify({"message": "Enter a string value for request and department"})
		if len(request.split()) == 0 or len(department.split())==0:
			return jsonify({"message": "Invalid entry try again"})
		helper.insert_user_request(request, department)
		res = helper.admin_get_all_requests()
		return jsonify({"res":res})


class RequestView(Resource):
	def get(self, request_id):
		res = helper.get_user_request(request_id)
		if res is None or len(res) == 0:
			return jsonify({"message":"Request not found"})
		return jsonify({"res":res})


class ModifyRequest(Resource):
	# //CAN ONLY MODIFY IF STATUS IS APPROVE 

	def put(self, request_id):
		parser = reqparse.RequestParser()
		parser.add_argument('request', type=str, help='invalid request')
		args = parser.parse_args()

		request = args['request']

		res = helper.get_user_request(request_id)
		if res is None or len(res) == 0:
			return jsonify({"message": "Request does not exist"})
		helper.modify_user_request(request_id)
		helper.get_request_by_id(request_id)
		items= cur.fetchone()
		return jsonify({"items":items})


class DeleteRequest(Resource):
	def delete(self, request_id):
		res = helper.get_user_request(request_id)
		if res is None or len(res) == 0:
			return jsonify({"message":"Request does not exist!"})
		helper.delete_request_by_id(request_id)
		helper.admin_get_all_requests()
		return jsonify({"message":"Deleted successfully"})


class ViewAllRequest(Resource):
	def get(self):
		res = helper.user_get_all()
		if res is None or len(res) == 0:
			return "No requests available"
		return jsonify({"res":res})

	
class AdminGetRequest(Resource):
	@jwt_required
	def get(self):
		helper.admin_get_all_requests()
		if res is None or len(res) == 0:
			return "No requests available"
		return jsonify({"res":res})


class ApproveRequest(Resource):
	@jwt_required		
	def put(self, request_id):
		res = get_request_by_id(request_id)
		if res is None:
			return jsonify({"message":"Request does not exist"})
		helper.approve_request_by_id(request_id)
		helper.get_request_by_id(request_id)
		items= cur.fetchone()
		return jsonify({"items":items})


class DisapproveRequest(Resource):
	@jwt_required
	def put(self, request_id):
		get_request_id(request_id)
		if res is None:
			return jsonify({"message":"Request does not exist"})
		helper.disapprove_request_by_id(request_id)
		helper.get_request_by_id(request_id)
		items= cur.fetchone()
		return jsonify({"items":items})


class AdminResolveRequest(Resource):
	@jwt_required
	def put(self, request_id):
		res = helper.get_request_by_id(request_id)
		if res is None or len(res)==0:
			return jsonify({"message":"Request does not exist"})
		helper.resolve_request_by_id(request_id)
		helper.get_request_by_id(request_id)
		items= cur.fetchone()
		return jsonify({"items":items})


class AdminDeleteRequest(Resource):
	@jwt_required
	def delete(self, request_id):
		helper.get_request_by_id(request_id)
		res = cur.fetchone()
		if res is None or len(res) == 0:
			return "Request does not exist!"
		helper.delete_request_by_id(request_id)
		helper.admin_get_all_requests()
		return jsonify({"message":"Deleted successfully"})

if __name__ == '__main__':
	print(User_login().get_one_user("kiki"))