from flask import Flask, jsonify, request
from models.admin import Admin
from models.user import User


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'working':'yes'}), 200

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    '''api endpoint for the user sign up'''
    post_new = request.get_json(force=True)
    new_user = User().sign_up(
        post_new['username'], post_new['email'], post_new['password'])
    return jsonify({'message': new_user}), 201

@app.route('/api/v1/login', methods=['POST'])
def login():
    '''api endpoint for user log in'''
    post_log = request.get_json(force=True)
    user_log_in = User().login(
        post_log['username'], post_log['password'])
    return jsonify({'message': user_log_in}), 201

@app.route('/api/v1/request', methods=['POST'])
def makerequest():
    '''api endpoint for user to make a request'''
    post_req = request.get_json(force=True)
    make_request = User().make_request(
        post_req['request_id'], post_req['request'], post_req['department'])
    return jsonify({'message': make_request})

@app.route('/api/v1/request/<int:request_id>', methods=['GET'])
def view_1(request_id):
    '''api endpoint for user to view a request'''
    result = User().view_a_request(request_id)
    return jsonify({'message': result})

@app.route('/api/v1/request', methods=['GET'])
def view():
    '''api endpoint for user viewing ALL requests'''
    requests = User().view_all_requests()
    return jsonify({"message": requests})

@app.route('/api/v1/request/<int:request_id>', methods=['PUT'])
def modify(request_id):
    '''api endpoint for user to modify a request'''
    post_mod = request.get_json(force=True)
    modify = User().modify_request(
        post_mod['request_id'], post_mod['new request'])
    return jsonify({'message': modify})

@app.route('/api/v1/request/<int:request_id>', methods=['DELETE'])
def delete_a_request(request_id):
    '''api endpoint for user to delete a request'''
    delete = User().delete_request(request_id)
    return jsonify({'message': delete})

@app.route('/api/v1/adminrequest', methods=['GET'])
def receive_request():
    '''api endpoint for admin to view incoming requests''' 
    requests = Admin().received_request()
    return jsonify({'message': requests})

    

if __name__ == "__main__":
    app.run(debug=True)
    