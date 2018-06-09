import unittest
import run
from manage import create_tables,cur,conn
import json
import models
from run import create_app


class TestModels(unittest.TestCase):
    """Test models for verion 2 api"""

    def setUp(self):
    	create_tables()
    	self.app = create_app()
    	self.checker = self.app.test_client()
    	self.request = {"request":"bulb repair","department":"hr", "status": "Pending"}
    	self.user = {"username": "kenny", "email": "kenny@gmail.com", "password": "kenny254"}

    def test_api_signup(self):
    	res = self.checker.post('/auth/signup', data = self.user)
    	result = json.loads(res.data.decode())
    	self.assertEqual(result['message'], "User successfully signed up")
    	self.assertEqual(res.status_code, 201)

    def test_user_already_exists(self):
    	'''Test user cannot be registered twice'''
    	res = self.checker.post('/auth/signup', data=self.user)
    	self.assertEqual(res.status_code, 201)
    	res2 = self.checker.post('/auth/signup', data=self.user)
    	self.assertEqual(res2.status_code, 202)
    	# getting results in json format
    	result = json.loads(res2.data.decode())
    	self.assertEqual(result['message'], 'The user already exists')

    def test_api_login(self):
    	res = self.checker.post('/auth/login', data=self.user)
    	self.assertEqual(res.status_code, 201)
    	login_res = self.checker.post('auth/login', data=self.user)
    	#get result in json format
    	result = json.loads(login_res.data.decode())
    	self.assertEqual(result['message'], "you have logged in successfully")
    	self.assertEqual(login_res.status_code, 200)
    	self.assertTrue(result['access_token'])

    def test_non_registered_user_login(self):
    	none_user = {'email': 'jwan', 'password': 'jwan254'}
    	res = self.checker.post('auth/login', data=none_user)
    	result = json.loads(res.data.decode())
    	self.assertEqual(res.status_code, 401)
    	self.assertEqual(result['message'], "You are not a user")

    def test_api_user_make_request(self):
    	res = self.checker.post('/users/requests', data=self.request)
    	self.assertEqual(res.status_code, 201)
    	self.assertIn("bulb repair", str(res.data))

    def test_api_user_view_a_request(self):
    	rv = self.checker.post('/users/requests', data=self.request)
    	self.assertEqual(rev.status_code, 201)
    	response = json.loads(rev.data.decode('utf-8').replace("'", "\""))
    	res = self.checker.get('/users/requests/{}'.format(response['request_id']))
    	self.assertEqual(res.status_code, 200)
    	self.assertIn("bulb repair", str(res.data))

    def test_api_user_view_all_requests(self):
    	res = self.checker.post('/users/requests', data=self.request)
    	self.assertEqual(res.status_code, 201)
    	res = self.checker.get('/users/requests')
    	self.assertEqual(res.status_code, 200)
    	self.assertIn("bulb repair", str(res.data))

    def test_api_user_modify_a_request(self):
    	res = self.checker.post('/users/requests', data={"request": "wiring repair", "department":"finance"})
    	self.assertEqual(rv.status_code, 201)
    	rv = self.checker.put('/users/request/1', data={"request": "container repair", "department":"finance"})
    	self.assertEqual(rv.status_code, 200)
    	res = self.checker.get('/users/requests/1')
    	self.assertIn("container repair", str(res.data))

    def test_api_user_delete_a_request(self):
    	rv = self.checker.post('/users/requests', data={"request":"bobby pins", "department":"hr"})
    	self.assertEqual(rv.status_code, 201)
    	res = self.checker.delete('/users/requests/1')
    	self.assertEqual(res.status_code, 200)
    	#testing to see if the deleted request exists
    	req = self.checker.get('/users/requests/1')
    	self.assertEqual(req.status_code, 404)

    def test_api_admin_view_requests(self):
    	res = self.checker.get('/users/requests')
    	self.assertEqual(res.status_code, 200)
    	self.assertIn("bulb repair", str(res.data))

    def test_admin_approve_request(self):
    	res = self.checker.get('/requests/1')
    	self.assertEqual(res.status_code, 200)
    	rv = self.checker.put('/users/request/1', data={"status": "Approved"})
    	self.assertEqual(rv.status_code, 200)
    	res = self.checker.get('/users/requests/1')
    	self.assertIn("Approved", str(res.data))

    def test_admin_reject_request(self):
    	res = self.checker.get('/requests/1')
    	self.assertEqual(res.status_code, 200)
    	rv = self.checker.put('/users/request/1', data={"status": "Rejected"})
    	self.assertEqual(rv.status_code, 200)
    	res = self.checker.get('/users/requests/1')
    	self.assertIn("Rejected", str(res.data))

    def test_admin_resolve_request(self):
    	res = self.checker.get('/requests/1')
    	self.assertEqual(res.status_code, 200)
    	rv = self.checker.put('/users/request/1', data={"status": "Resolved"})
    	self.assertEqual(rv.status_code, 200)
    	res = self.checker.get('/users/requests/1')
    	self.assertIn("Resolved", str(res.data))

    def test_admin_delete_request(self):
    	rv = self.checker.get('/requests/1')
    	self.assertEqual(rv.status_code, 200)
    	res = self.checker.delete('/users/requests/1')
    	self.assertEqual(res.status_code, 200)
    	#testing to see if the deleted request exists
    	req = self.checker.get('/users/requests/1')
    	self.assertEqual(req.status_code, 404)

    def tearDown(self):
    	try:
    		cur.execute("DROP TABLE IF EXISTS users")
    		cur.execute("DROP TABLE IF EXISTS requests")
    		conn.commit()
    	except:
    		print("cannot delete tables")

if __name__ == '__main__':
	unittest.main()