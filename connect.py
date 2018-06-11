import psycopg2
from config import config

def connect():
	conn = None
	try:
		params = config()

		print('Connecting to psql db')
		conn = psycopg2.connect(**params)
		cur = conn.cursor

		# print("")