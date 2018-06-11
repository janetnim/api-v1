import psycopg2


conn = psycopg2.connect("dbname='maintenance' user='postgres' host='localhost' password='123456'")
cur = conn.cursor()


def create_tables():
	try:

		cur.execute("CREATE TABLE IF NOT EXISTS users (personal_id serial PRIMARY KEY, username varchar unique NOT NULL, email varchar unique NOT NULL, password varchar unique NOT NULL)")
		cur.execute("CREATE TABLE IF NOT EXISTS requests (request_id serial PRIMARY KEY, request varchar, department varchar, status varchar, personal_id integer REFERENCES users (personal_id))")
		cur.execute("SELECT * FROM users WHERE username != 'admin'")

		conn.commit()

	except:
		print("Cannot connect to database")



create_tables()