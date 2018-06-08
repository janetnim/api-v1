from flask_restful import Resource, reqparse
from  flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from flask import jsonify
from manage import create_tables,cur,conn
import psycopg2
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

		if username=="" or email=="" or password=="":
			return "Please enter all details"
		cur.execute("SELECT username FROM users;")
		res = cur.fetchall()
		if username in res:
			return "The user already exists"
		cur.execute("INSERT INTO users (username, email, password) VALUES('{}','{}','{}')".format(username, email, password))
		cur.execute("SELECT * FROM users WHERE username  = %s",(username,))
		conn.commit()
		return "User successfully signed up"

class User_login(Resource):
	def get_one_user(self, username):
		cur.execute("SELECT * FROM users WHERE username =%s", (username,))
		user = cur.fetchone()
		conn.commit()
		return{
			"personal_id":user[0],
			"username":user[1],
			"email":user[2],
			"password":user[3]
		}

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, help='invalid username')
		parser.add_argument('password', type=str, help='invalid password')
		args = parser.parse_args()

		username = args['username']
		password = args['password']

		cur.execute("SELECT * FROM users WHERE username = %s AND password = %s ", (username,password))


		user = User_login().get_one_user(username)
		if user is None:
			return jsonify({"message":"user not found"}), 404
		elif user['password'] != password:
			return jsonify({"message":"incorrect password"})
		else:
			token = create_access_token(identity=username)
			return jsonify({"message": "logged in successfully", "token":token})
		return make_response("cannot verify", 401, {"WWW-Authentication": "Basic realm='Login required'"})

		if username=="" or password=="":
			return jsonify({"message":"Enter all details"})
		cur.execute("SELECT username FROM users")
		res = cur.fetchall()
		if username not in res:
			return jsonify({"message":"You are not a user"})
		conn.commit()
		return jsonify({"message":"you have logged in successfully"})


class MakeRequest(Resource):
	@jwt_required
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('request', type=str, help='invalid request')
		parser.add_argument('department', type=str, help='invalid department')
		parser.add_argument('status', type=str, help='invalid status')
		parser.add_argument('personal_id', type=str, help='invalid id')
		args = parser.parse_args()

		request = args['request']
		department = args['department']
		status = args['status']
		personal_id = args['personal_id']

		if request=="" or department=="" or status=="" or personal_id == "":
			return jsonify({"message":"Please fill all details"})
		cur.execute("INSERT INTO requests (request, department, status, personal_id)VALUES('{}','{}','Pending', {})".format(request, department, personal_id))
		cur.execute("SELECT * FROM requests")
		res = cur.fetchall()
		conn.commit()
		return jsonify({"res":res})


class RequestView(Resource):
	@jwt_required
	def get(self, request_id, personal_id):
		cur.execute("SELECT * FROM requests WHERE request_id={} and personal_id={}".format(request_id, personal_id))
		res = cur.fetchone()
		if res is None or len(res) == 0:
			return jsonify({"message":"Request not found"})
		return jsonify({"res":res})


class ModifyRequest(Resource):
	@jwt_required
	def put(self, request_id, personal_id):
		parser = reqparse.RequestParser()
		parser.add_argument('request', type=str, help='invalid request')
		args = parser.parse_args()

		request = args['request']

		cur.execute("SELECT * FROM requests WHERE request_id={} and personal_id={}".format(request_id, personal_id))
		res = cur.fetchone()
		if res is None or len(res) == 0:
			return jsonify({"message": "Request does not exist"})
		cur.execute("UPDATE requests SET request={} WHERE request_id={} and personal_id={}".format(request, request_id, personal_id));
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		conn.commit()
		items= cur.fetchone()
		return jsonify({"items":items})


class DeleteRequest(Resource):
	@jwt_required
	def delete(self, request_id, personal_id):
		cur.execute("SELECT * FROM requests WHERE request_id={} and personal_id={}".format(request_id, personal_id))
		res = cur.fetchone()
		if res is None or len(res) == 0:
			return "Request does not exist!"
		cur.execute("DELETE  FROM requests WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests")
		conn.commit()
		return jsonify({"message":"Deleted successfully"})


class ViewAllRequest(Resource):
	@jwt_required
	def get(self, personal_id):
		cur.execute("SELECT * FROM requests WHERE personal_id={}".format(personal_id))
		res =cur.fetchall()
		if res is None or len(res) == 0:
			return "No requests available"
		return jsonify({"res":res})

	
class AdminGetRequest(Resource):
	@jwt_required
	def get(self):
		cur.execute("SELECT * FROM requests")
		res =cur.fetchall()
		if res is None or len(res) == 0:
			return "No requests available"
		return jsonify({"res":res})


class ApproveRequest(Resource):
	@jwt_required		
	def put(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res=cur.fetchone()
		if res is None:
			return jsonify({"message":"Request does not exist"})
		cur.execute("UPDATE requests SET status='Approve' WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		conn.commit()
		items= cur.fetchone()
		return jsonify({"items":items})


class DisapproveRequest(Resource):
	@jwt_required
	def put(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res=cur.fetchone()
		if res is None:
			return jsonify({"message":"Request does not exist"})
		cur.execute("UPDATE requests SET status='Disapprove' WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		conn.commit()
		items= cur.fetchone()
		return jsonify({"items":items})


class AdminResolveRequest(Resource):
	@jwt_required
	def put(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res=cur.fetchone()
		if res is None:
			return jsonify({"message":"Request does not exist"})
		cur.execute("UPDATE requests SET status='Complete' WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		conn.commit()
		items= cur.fetchone()
		return jsonify({"items":items})


class AdminDeleteRequest(Resource):
	@jwt_required
	def delete(self, request_id):
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		res = cur.fetchone()
		if res is None or len(res) == 0:
			return "Request does not exist!"
		cur.execute("DELETE  FROM requests WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests")
		conn.commit()
		return jsonify({"message":"Deleted successfully"})

