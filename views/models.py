class Authentication(Resource):
	cur.execute("CREATE TABLE IF NOT EXISTS users (personal_id serial PRIMARY KEY, username varchar unique, email varchar unique, password varchar unique)")
	def post_signup(self, username="", email="", password=""):
		if username="" or email="" or password="":
			return "Please enter all details"
		cur.execute("SELECT username FROM users")
		res = cur.fetchall()
		if username in res:
			return "The user already exists"
		cur.execute("INSERT INTO users (username, email, password)VALUES('{}','{}','{}')".format(username, email, password))
		cur.execute("SELECT * FROM users WHERE username={}".format(username))
		conn.commit()
			return "User successfully signed up"

# CHANGE OUTPUT TO JSONIFY

	def post_login(self, username="", password=""):
		if username="" or password="":
			return "Enter all details"
		cur.execute("SELECT username FROM users")
		res = cur.fetchall()
		if username not in res:
			return "You are not a user"
		conn.commit()
		return "you have logged in successfully"
		# NOTE TO SELF: the above use api auth/signup or auth/login


class User(Resource):
	cur.execute("CREATE TABLE IF NOT EXISTS requests (request_id serial PRIMARY_KEY, request varchar, department varchar, personal_id integer REFERENCES users (personal_id))")
	cur.execute("SELECT * FROM users WHERE username != 'admin'")

	def post_make_request(self, request={}, department={}):
		if request="" or department="":
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
	

	def get_view_all_requests(self):
		cur.execute("SELECT * FROM requests")
		res =cur.fetchall()
		if res is None:
			return "No requests available"
		return res
		# NOTE TO SELF: the view all requests gets api/v2/users/requests
	

	def put_modify_request(self, request_id):
		cur.execute("SELECT request_id FROM requests WHERE request_id={}".format(request_id))
		res = cur.fetchone()
		if res is None:
			return "Request not present"
		cur.execute("UPDATE requests SET request='Computer replacement' WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		conn.commit()
		items= cur.fetchone()
		return items

	
	def delete_a_request(self, request_id):
		cur.execute("SELECT * FROM requests WHERE request_id={}".format(request_id))
		res = cur.fetchone()
		if res is None:
			return "Request does not exist!"
		cur.execute("DELETE * FROM requests WHERE request_id={}".format(request_id))
		cur.execute("SELECT * FROM requests")
		conn.commit()
		return "Deleted successfully"
	#NOTE TO SELF: the above use api/v2/users/requests/.... or api/v2/users/requests


# class Admin(Resource):
# 	cur.execute("CREATE TABLE IF NOT EXISTS admin (request_id serial PRIMARY_KEY, request varchar, department varchar)")
# 	cur.execute("SELECT * FROM admin WHERE username = 'admin'")
# 	admin = cur.fetchone()
# 	if admin is None:
# 		# cur.execute("INSERT INTO(request, department)VALUES('{}','{}')".format(request,department))

# 	def get_all_requests:
# 		res = cur.execute("SELECT * FROM admin")
# 		if res is None:
# 			return "No requests available"
# 		items = cur.fetchall()
# 		return items

# 	def put_approve_request:
# 		pass
# 	def put_disapprove_request:
# 		pass
# 	def put_resolve_request:
# 		pass 
# 	NOTE TO SELF: the above uses the api: api/v2/requests/<reqid>/<resolve/disapprove/approve>
# 	NOTE TO SELF: while view all requests is api/v2/requests

api.add_resource(Authenication, 'api/v2/auth/')
api.add_resource(User, 'api/v2/users/requests')
api.add_resource(User, 'api/v2/users/requests/<int:request_id>')
api.add_resource(Admin, 'api/v2/requests')
api.add_resource(Admin, 'api/v2/requests/<int:request_id>')
# cur.close()
# con.close()