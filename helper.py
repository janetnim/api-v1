import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.handlers.bcrypt import bcrypt
import os

class Database:

	def __init__(self):
		self.conn = None
		self.cur = None

	def initialize(self,app):
		database_name = app.config['DATABASE_NAME']
		self.conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(
			app.config['DATABASE_NAME'],
			app.config['DATABASE_USER'],
			app.config['DATABASE_HOST'],
			app.config['DATABASE_PASSWORD']))
		self.cur = self.conn.cursor(cursor_factory = RealDictCursor)

		self.cur.execute("CREATE TABLE IF NOT EXISTS users (personal_id serial PRIMARY KEY, username varchar  NOT NULL, email varchar  NOT NULL, password varchar  NOT NULL, role varchar)")
		self.cur.execute("CREATE TABLE IF NOT EXISTS requests (request_id serial PRIMARY KEY, request varchar, "\
			"department varchar, status varchar, personal_id integer REFERENCES users (personal_id) ON DELETE CASCADE)")
		self.cur.execute("SELECT * FROM users WHERE username = 'admin'")
		result = self.cur.fetchone()
		if result is None:
			self.cur.execute("INSERT INTO users(username,email,password,role) VALUES('admin', 'admin@gmail.com','{}','admin');".format(bcrypt.encrypt("admin254")))
		self.conn.commit()

	def drop_everything(self):
		self.cur.execute("DROP TABLE requests;")
		self.cur.execute("DROP TABLE users;")
		self.conn.commit()

	def add_user(self,username,password, email):
		self.cur.execute("INSERT INTO users(username,email,password,role) VALUES (%s, %s, %s, 'user') RETURNING personal_id;", (username, email, password))
		self.conn.commit()
		result = self.cur.fetchone()
		return result['personal_id']

	def get_user_by_username(self,username):
		self.cur.execute("SELECT * FROM users WHERE username = %s;", (username,))
		result = self.cur.fetchone()
		self.conn.commit()
		return result

	def get_user(self, username):
		self.cur.execute("SELECT username FROM users WHERE username=%s",(username,))
		return self.cur.fetchone()

	def get_users_by_username(self):
		self.cur.execute("SELECT username FROM users")
		res = self.cur.fetchall()
		self.conn.commit()
		return res

	def get_user_request(self,request_id, personal_id):
		self.cur.execute("SELECT * FROM requests WHERE request_id=%s and personal_id=%s",(request_id,personal_id,))
		return self.cur.fetchone()

	def get_user_by_status(self):
		self.cur.execute("SELECT status FROM requests WHERE status='Pending'")
		return self.cur.fetchone()

	def get_user_by_username_and_password(self,username, password):
		self.cur.execute("SELECT * FROM users WHERE username = %s",(username,))
		result = self.cur.fetchone()
		if result is None:
			return None
		if bcrypt.verify(password, result["password"]):
			return result
		return None

	def get_users(self):
		self.cur.execute("SELECT * FROM users WHERE username!='admin'")
		res = self.cur.fetchall()
		return res

	def get_role(self, username):
		self.cur.execute("SELECT role FROM users WHERE username = %s", (username,))
		result = self.cur.fetchone()
		return result

	def get_user_by_personal_id(self):
		self.cur.execute("SELECT * FROM users WHERE personal_id= %s", (personal_id,))
		return self.cur.fetchone()

	def post_request(self,request, department, status):
		self.cur.execute("INSERT INTO requests(request,department,status) VALUES(%s, %s, 'Pending') RETURNING request_id", (request, department))
		res = self.cur.fetchone()
		self.conn.commit()
		return result['request_id']

	def get_request_by_id(self,request_id):
		self.cur.execute("SELECT * FROM requests WHERE request_id = %s",(request_id,))
		return self.cur.fetchone()

	def get_request_id(self):
		self.cur.execute("SELECT request_id FROM requests WHERE request_id=%s",(request_id,))
		res=self.cur.fetchone()
		return res

	def user_get_all(self,personal_id):
		self.cur.execute("SELECT * FROM requests WHERE personal_id = %s", (personal_id,))
		res = self.cur.fetchall()
		return res

	def put_modify_request_by_id(self,request_id):
		self.cur.execute("UPDATE requests SET request = %s WHERE request_id = %s", (request, request_id,))
		res = self.cur.fetchone()
		self.conn.commit()
		return res

	def delete_request_by_id(self,request_id):
		self.cur.execute("DELETE  FROM requests WHERE request_id = %s", (request_id,))
		self.conn.commit()

	def approve_request_by_id(self,request_id):
		self.cur.execute("UPDATE requests SET status='Approve' WHERE request_id=%s",(request_id,))
		self.conn.commit()

	def disapprove_request_by_id(self,request_id):
		self.cur.execute("UPDATE requests SET status='Disapprove' WHERE request_id=%s",(request_id,))
		self.conn.commit()

	def resolve_request_by_id(self,request_id):
		self.cur.execute("UPDATE requests SET status='Resolved' WHERE request_id=%s",(request_id,))
		self.conn.commit()

	def admin_get_all_requests(self,):
		self.cur.execute("SELECT * FROM requests;")
		req = self.cur.fetchall()
		return req

	def admin_get_approved_requests(self):
		self.cur.execute("SELECT * FROM requests WHERE status='Approve'")
		req = self.cur.fetchall()
		return req

	def admin_get_rejected_requests(self):
		self.cur.execute("SELECT * FROM requests WHERE status='Disapprove'")
		req = self.cur.fetchall()
		return req

	def admin_get_resolved_requests(self):
		self.cur.execute("SELECT * FROM requests WHERE status='Resolved'")
		req = self.cur.fetchall()
		return req

	def insert_user_request(self,request, department, personal_id):
		self.cur.execute("INSERT INTO requests (request, department, status, personal_id) VALUES(%s,%s,'Pending', %s) RETURNING request_id",(request, department,personal_id))
		result = self.cur.fetchone()
		self.conn.commit()
		return result['request_id']

	def modify_user_request(self,request_id, request):
		self.cur.execute("UPDATE requests SET request = %s WHERE request_id = %s", (request, request_id,))
		self.conn.commit()

helper = Database()
