import os
from flask import Flask, jsonify, request, abort
from models.admin import admin
from models.user import User

app = Flask(__name__)

'''api endpoint for the user sign up'''
@app.route('api/v1/login', methods=['POST'])
def signup():
	if request.json:
		new_user = User().signup(request.json['username'], request.json['email'], request.json['password'])
		return jsonify({'New_user': new_user})
	new_user = User().signup(request.form.get('username'), request.form.get('email'), request.form.get('password'))
	return jsonify({'New_user': new_user})

'''api endpoint for user log in'''
@app.route('api/v1/login', methods=['POST'])
def login():
	if request.json:
		user_log_in = User().login(request.json['username'], request.json['password'])
		return jsonify({'User': user_log_in})
	user_log_in = User().login(request.form.get('username'), request.form.get('password'))
	return jsonify({'User': user_log_in})

'''api endpoint for user to make a request'''
@app.route('api/v1/makerequest/', methods=['POST'])
def makerequest():
    if request.json:
		make_request = User().make_request(request.json['request_id'], request.json['request'], request.json['department'])
		return jsonify({'Requests made': make_request})
	make_request = User().make_request(request.form.get('request_id'), request.form.get('request'), request.form.get('department'))
	return jsonify({'Requests made': make_request})

'''api endpoint for user to view a request'''
@app.route('api/v1/view/<int:requestid>', methods=['GET'])
def view(request_id):
    @app.route('api/v1/view/<int:requestid>', methods=['GET'])
    request = [request for request in request_data if request_data['id'] == requestid]
    if len(request) == 0:
        abort(404)
    return jsonify{'request': request['requestid']}

'''api endpoint for user viewing all requests'''
@app.route('api/v1/viewAll/', methods=['GET'])
def viewAll():
	requests = User().view_all_requests()
	return jsonify({"Requests": })

'''api endpoint for user to modify a request'''
@app.route('api/v1/modify/<int:requestid>', methods=['PUT'])
def modify(request_id):
	if request.json:
		modify = User().modify_request(request.json['request_id'], request.json['request'], request.json['department'])
		return jsonify({'Requests': modify})
	modify = User().modify(request.form.get('requestid'), request.form.get('request'), request.json['department'])
	return jsonify({'Requests modidfied': modify})

'''api endpoint for user to delete a request'''
@app.route('api/v1/delete/<int:requestid>', methods=['DELETE'])
def delete_a_request(request_id):
	delete = User().request_data.remove(request_id)
	return jsonify{'Requests deleted': delete}

if '__name__' == '__main__':
	app.run(debug = True)
