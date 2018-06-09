import unittest
from run import create_app
import json

class TestModels(unittest.TestCase):
    """Test models for verion 2 api"""

    def setUp(self):
        self.client = create_app().test_client()
        self.headers = {"Content-Type": "application/json"}


    def test_user_signup_with_empty_details(self):
        data = dict(username="schrodinger", email='cat@gmail.com', password='2547')
        response = self.client.post('/auth/signup', data=json.dumps(data), headers=self.headers)

        json_result = json.loads(response.get_data(as_text=True))
        self.assertEqual(200, response.status_code)
        self.assertEqual("User successfully signed up", json_result['message'])


    def test_user_login(self):
        credentials = dict(username='admin', password='admin254')
        response = self.client.post('/auth/login', data=json.dumps(credentials), headers=self.headers)
        
        json_result = json.loads(response.get_data(as_text=True))
        self.assertEqual(200, response.status_code)
        self.assertEqual("logged in successfully", json_result['message'])
        self.assertIn("token", json_result)

    # def test_user_login(self):
    #     credentials = dict(username='', password='')
    #     response = self.client.post('/auth/login', data=credentials)
    #     print(response.data)
    #     self.assertEqual(b'Enter all details', 'Enter all details')

    # def test_user_make_request(self):

    # 	pass
    # def test_user_view_a_request(self):
    # 	pass
    # def test_user_view_all_requests(self):
    # 	pass
    # def test_user_modify_a_request(self):
    # 	pass
    # def test_user_delete_a_request(self):
    # 	pass
    # def test_admin_view_requests(self):
    # 	data = request.json.get
    # 	pass
    # def test_admin_approve_request(self):
    # 	pass
    # def test_admin_reject_request(self):
    # 	pass
    # def test_admin_resolve_request(self):
    # 	pass
    # def test_admin_delete_request(self):
    # 	pass