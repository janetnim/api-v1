from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from config import config
import psycopg2
from views.models import User
from views.models import Request
from test.test_api import TestModels
# import manage.py

app = Flask(__name__)
api = Api(app)

conn = psycopg2.connect(dbname='maintenance' user='janetnim' host='localhost' password='icarly401')
cur = conn.cursor()

api.add_resource(Authenication, 'api/v2/auth/')
api.add_resource(User, 'api/v2/users/requests')
api.add_resource(User, 'api/v2/users/requests/<int:request_id>')
api.add_resource(Admin, 'api/v2/requests')
api.add_resource(Admin, 'api/v2/requests/<int:request_id>')

if __name__ == '__main__':
	app.run(debug=True)
