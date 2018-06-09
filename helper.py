import psycopg2
import psycopg2.extras
from manage import create_tables, cur, conn


create_tables()

def add_user(username,password, email):
	cur.execute("INSERT INTO users(username,email,password) VALUES (%s, %s, %s) RETURNING personal_id;", (username, email, password))
	conn.commit()
	result = cur.fetchone()
	return result['personal_id']

def get_user_by_username(username):
	cur.execute("SELECT * FROM users WHERE username = %s", (username,))
	result = cur.fetchone()
	conn.commit()
	return result

def get_users_by_username():
	cur.execute("SELECT username FROM users")
	res = cur.fetchall()
	conn.commit()
	return res

def get_user_request(request_id):
	cur.execute("SELECT * FROM requests WHERE request_id=%s",(request_id,))
	cur.fetchone()

def get_user_by_username_and_password(username, password):
	cur.execute("SELECT * FROM users WHERE username = %s and password = %s",(username, password,))
	return cur.fetchone()

def post_request(request, department, status):
	cur.execute("INSERT INTO requests(request,department,status) VALUES(%s, %s, 'Pending') RETURNING request_id", (request, department))
	res = cur.fetchone()
	conn.commit()
	return result['request_id']

def get_request_by_id(request_id):
	cur.execute("SELECT * FROM requests WHERE request_id = %s",(request_id,))
	return cur.fetchone()

def get_request_id():
	cur.execute("SELECT request_id FROM requests WHERE request_id=%s",(request_id,))
	res=cur.fetchone()
	return res

def user_get_all():
	cur.execute("SELECT * FROM requests")
	res = cur.fetchall()
	return res

def put_modify_request_by_id(request_id):
	cur.execute("UPDATE requests SET request = %s WHERE request_id = %s", (request, request_id,))
	res = cur.fetchone()
	conn.commit()
	return res

def  delete_request_by_id(request_id):
	cur.execute("DELETE  FROM requests WHERE request_id = %s", (request_id,))
	conn.commit()

def approve_request_by_id(request_id):
	cur.execute("UPDATE requests SET status='Approve' WHERE request_id=%s",(request_id,))
	conn.commit()

def disapprove_request_by_id(request_id):
	cur.execute("UPDATE requests SET status='Disapprove' WHERE request_id=%s",(request_id,))
	conn.commit()

def resolve_request_by_id(request_id):
	cur.execute("UPDATE requests SET status='Resolved' WHERE request_id=%s",(request_id,))
	conn.commit()

def admin_get_all_requests():
	cur.execute("SELECT * FROM requests")
	cur.fetchall()

def insert_user_request(request, department, personal_id):
	cur.execute("INSERT INTO requests (request, department, status)VALUES(%s,%s,'Pending') RETURNING request_id",(request, department,))
	conn.commit()

def modify_user_request(request_id, personal_id):
	cur.execute("UPDATE requests SET request = %s WHERE request_id = %s", (request, request_id,))
	conn.commit()





if __name__ == '__main__':
	print(get_user_by_username("kiki"))