from flask_restful import Resource, reqparse
from  flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from flask import jsonify


class User_SignUp(Resource):
	def post_signup(self, username, email, password):
		if username=="" or email=="" or password=="":
			return "Please enter all details"
		cur.execute("SELECT username FROM users")
		res = cur.fetchall()
		if username in res:
			return "The user already exists"
		password = generate_password_hash((password), method='sha256')
		cur.execute("INSERT INTO users (username, email, password)VALUES('{}','{}','{}')".format(username, email, password))
		cur.execute("SELECT * FROM users WHERE username={}".format(username))
		conn.commit()
		return "User successfully signed up"

class User_login(Resource):
	def get_one_user(self):
		cur.execute("SELECT * FROM usrs WHERE username =%s", (username,))
		user = cur.fetchone()
		conn.commit()
		return{
		"personal_id":user[0],
		"username":user[1],
		"email":user[2],
		"password":user[3]
		}

	def post(self):
		username = request.json.get("username")
		password = request.json.get("password")

		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, help='invalid username')
		args = parser.parse_args()

		user = get_user(username)
		if user is None:
			return jsonify({"message":"user not found"}), 404
		elif user['password'] != password:
			return jsonify({"message":"incorrect password"})
		else:
			token = create_access_token(identity=request.json.get("username"))
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


class Request(Resource):
	def post_make_request(self, request={}, department={}, status="Sent"):
		if request=="" or department=="":
			return "Please fill all details"
		cur.execute("INSERT INTO user(request, department)VALUES('{}', '{}')".formart(request, department))
		cur.execute("SELECT * FROM requests")
		res = cur.fetchone()
		conn.commit()
		return res


	def get_view_a_request(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res = cur.fetchone()
		if res is None:
			return "Request not found!"
		return res
	

	def get_view_all_requests(self, personal_id):
		cur.execute("SELECT * FROM requests WHERE personal_id={}".format(personal_id))
		res =cur.fetchall()
		if res is None:
			return "No requests available"
		return res
	

	def put_modify_request(self, request_id, personal_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}, personal_id={}".format(request_id, personal_id))
		res = cur.fetchone()
		if res is None:
			return "Request not present"
		cur.execute("UPDATE requests SET request='Computer replacement' WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		conn.commit()
		items= cur.fetchone()
		return items

	
	def delete_a_request(self, request_id, personal_id):
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id, personal_id))
		res = cur.fetchone()
		if res is None:
			return "Request does not exist!"
		cur.execute("DELETE * FROM requests WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests")
		conn.commit()
		return "Deleted successfully"

	def get_all_requests_admin(self):
		cur.execute("SELECT * FROM requests")
		res =cur.fetchall()
		if res is None:
			return "No requests available"
		return res
		
	def put_approve_request(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res=cur.fetchone()
		if res is None:
			return "Request not present"
		# change status to approve
		# then commit

	def put_disapprove_request(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res=cur.fetchone()
		if res is None:
			return "Request not present"
		# change status to disapprove
		# then commit

	def put_resolve_request(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res=cur.fetchone()
		if res is None:
			return "Request not present"
		# change status to complete
		# then commit

	def delete_request(self, request_id):
		pass


		# cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		# res=cur.fetchone()
		# if res is None:
		# 	return "Request not present"
		# change status to approve
		# if status is complete, delete then commit
