import unittest
import json
from api import app
from models.admin import Admin
from models.user import User


class User(unittest.TestCase):
    def setUp(self):
        self.checker = app.test_client()

    def test_user_sign_up(self):
        # testing user sign up entries -post
        details = {"email": "janetnim401@gmail.com",
                   "username": "janet", "password": 12345}
        response = self.checker.post(
            '/api/v1/signup', data=json.dumps(details), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_log_in(self):
        # testing user log in entries -post
        details = {"username": "janet", "password": 66555}
        response = self.checker.post(
            '/api/v1/login', data=json.dumps(details), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_make_request(self):
        # testing user make a request -post
        request_data = {1255, "machine fixing", "finance"}
        response = self.checker.post(
            '/api/v1/make_request', data=json.dumps(request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_view_a_request(self):
        # testing user viewing each request -get
        request_data = {1234}
        response = self.checker.post(
            '/api/v1/view/1234', data=json.dumps(User().request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_view_all_requests(self):
        # testing user view all his requests -get
        response = self.checker.post(
            '/api/v1/view', data=json.dumps(User().request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_modify_request(self):
        # testing user modify a request -update
        request_data = {5555}
        response = self.checker.post(
            '/api/v1/modify/1234', data=json.dumps(User().request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_delete_a_request(self):
        # testing a user delete a request -delete
        request_data = {5478}
        response = self.checker.post(
            '/api/v1/delete/1234', data=json.dumps(User().request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)


class Admin(unittest.TestCase):
    '''def test_receive_request(self):
        # testing an admin receive requests from users -get
        received_requests = {7777, "curtains repair", "media"}
	    response = self.checker.post('/api/v1/adminrequest/7777', data=json.dumps(
	        received_requests), content_type='application/json')
	    self.assertEqual(response.status_code, 201)'''
    def setUp(self):
	    self.checker = app.test_client()

    def test_view_request(self):
        # testing an admin view all requests sent -get
	    response = self.checker.post(
	        '/api/v1/adminview', data=json.dumps(Admin().received_requests), content_type='application/json')
	    self.assertEqual(response.status_code, 201)
'''
    def test_resolve_request(self):
        # testing an admin resolve each relevant request
        received_requests = {1234}
	    response = self.checker.post(
	        '/api/v1/resolve/1234', data=json.dumps(received_requests), content_type='application/json')
	    self.assertEqual(response.status_code, 201)'''


if __name__ == '__main__':
    unittest.main()
