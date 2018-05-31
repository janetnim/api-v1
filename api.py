import os
from flask import Flask, jsonify, request, abort
from models.admin import Admin
from models.user import User


app = Flask(__name__)


@app.route('/api/v1/signup', methods=['POST'])
def signup():
    '''api endpoint for the user sign up'''
    post_new = request.get_json(force=True)
    new_user = User().sign_up(
        post_new['username'], post_new['email'], post_new['password'])
    return jsonify({'New_user': new_user}), 201


@app.route('/api/v1/login', methods=['POST'])
def login():
    '''api endpoint for user log in'''
    post_log = request.get_json(force=True)
    user_log_in = User().login(
        post_log['username'], post_log['password'])
    return jsonify({'User': user_log_in}), 201


@app.route('/api/v1/makerequest/', methods=['POST'])
def makerequest():
    '''api endpoint for user to make a request'''
    post_req = request.get_json(force=True)
    make_request = User().make_request(
        post_req['request_id'], post_req['request'], post_req['department'])
    return jsonify({'Requests made': make_request})


@app.route('/api/v1/view/<int:request_id>', methods=['GET'])
def view_1(request_id):
    '''api endpoint for user to view a request'''
    result = User().view_a_request(request_id)
    return jsonify({'request': result})


@app.route('/api/v1/view', methods=['GET'])
def view():
    '''api endpoint for user viewing ALL requests'''
    requests = User().view_all_requests()
    return jsonify({"Requests": requests})


@app.route('/api/v1/modify/<int:request_id>', methods=['PUT'])
def modify(request_id):
    '''api endpoint for user to modify a request'''
    post_mod = request.get_json(force=True)
    modify = User().modify_request(
        request_id, post_mod['request'])
    return jsonify({'Requests': modify})


@app.route('/api/v1/delete/<int:request_id>', methods=['DELETE'])
def delete_a_request(request_id):
    '''api endpoint for user to delete a request'''
    delete = User().delete_request(request_id)
    return jsonify({'Requests deleted': delete})


# @app.route('/api/v1/adminrequest', methods=['GET'])
# def receive_request(request_id):
#     '''api endpoint for admin to view incoming requests''' 
#     requests = User().received_request(request_id, request, department)
#     return jsonify({'request': request['request_id']})


# @app.route('/api/v1/adminview', methods=["GET"])
# def view_requests():
#     '''api endpoint for the admin to view all users requests'''
#     requests = Admin().view_all_requests()
#     return jsonify({'Requests': requests})


# @app.route('/api/v1/resolve/<int:request_id>', methods=['GET'])
# def resolve_request(request_id):
#     '''api endpoint for admin to get a request to resolve'''
#     request = [request for request in received_requests if received_requests['id'] == requestid]
#     if len(request) == 0:
#         abort(404)
#     return jsonify({'request': request['request_id']})


if __name__ == '__main__':
    app.run(debug=True)