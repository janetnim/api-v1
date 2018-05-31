import os
from flask import Flask, jsonify, request, abort
from models.admin import Admin
from models.user import User


app = Flask(__name__)

'''api endpoint for the user sign up'''


@app.route('/api/v1/signup', methods=['POST'])
def signup():
    post_new = request.get_json(force=True)
    if post_new:
        new_user = User().sign_up(
            post_new['username'], post_new['email'], post_new['password'])
        return jsonify({'New_user': new_user}), 201
    new_user = User().signup(request.form.get('username'),
                             request.form.get('email'), request.form.get('password'))
    return jsonify({'New_user': new_user})


'''api endpoint for user log in'''


@app.route('/api/v1/login', methods=['POST'])
def login():
    post_new = request.get_json(force=True)
    if post_log:
        user_log_in = User().login(
            post_log['username'], post_log['password'])
        return jsonify({'User': user_log_in}), 201
    user_log_in = User().login(request.form.get(
        'username'), request.form.get('password'))
    return jsonify({'User': user_log_in})


'''api endpoint for user to make a request'''


@app.route('/api/v1/makerequest/', methods=['POST'])
def makerequest():
    post_req = request.get_json(force=True)
    if post_req:
        make_request = User().make_request(
            post_req['request_id'], post_req['request'], post_req['department'])
        return jsonify({'Requests made': make_request})
        make_request = User().make_request(request.form.get('request_id'), request.form.get('request'), request.form.get('department'))
        return jsonify({'Requests made': make_request})


'''api endpoint for user to view a request'''


@app.route('/api/v1/view/<int:requestid>', methods=['GET'])
def view(request_id):
    request = [request for request in request_data if request_data['id'] == requestid]
    if len(request) == 0:
        abort(404)
    return jsonify({'request': request['requestid']})


'''api endpoint for user viewing ALL requests'''


@app.route('/api/v1/view', methods=['GET'])
def view():
    requests = User().view_all_requests()
    return jsonify({"Requests": requests})


'''api endpoint for user to modify a request'''


@app.route('/api/v1/modify/<int:requestid>', methods=['PUT'])
def modify(request_id):
    post_mod = request.get_json(force=True)
    if post_mod:
        modify = User().modify_request(
            post_mod['request_id'], request.json['request'], post_mod['department'])
        return jsonify({'Requests': modify})
    modify = User().modify(request.form.get('requestid'),
                           request.form.get('request'), request.json['department'])
    return jsonify({'Requests modidfied': modify})


'''api endpoint for user to delete a request'''


@app.route('/api/v1/delete/<int:requestid>', methods=['DELETE'])
def delete_a_request(request_id):
    delete = User().request_data.remove(request_id)
    return jsonify({'Requests deleted': delete})


if '__name__' == '__main__':
    app.run(debug=True)