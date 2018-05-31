import unittest
import json
from api import app


class User(unittest.TestCase):
	def setUp(self):
		checker = app.test_client()


		details = {"username":"janet", "password":"12345"}
		response = checker.post('/api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)


	def test_user_sign_up(self):
		# testing user sign up entries -post
		details = {"email":"janetnim401@gmail.com", "username":"janet", "password":"12345"}
		response = self.checker.post('/api/v1/signup', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully created an account")

		details_1 = {"email":" ", "username":" ", "password": " "}
		response_1 = self.checker.post('/api/v1/signup', data=json.dumps(details_1), content_type = 'application/json')
		self.assertEqual(response_1.status_code, 200)
		output_1 = json.loads(response_1.data)
		self.assertEqual(response_1, 200)
		self.assertEqual(output_1, "You have blank entries, please fill all details")

		details_2 = {"username":678887, "email": "janetnim401@gmail.com", "password": 12345}
		response_2 = self.checker.post('/api/v1/login', data=json.dumps(details_2), content_type = 'application/json')
		output_2 = json.loads(response_2.data)
		self.assertEqual(response_2, 200)
		self.assertEqual(output_2, "Please use data in string format for username")

		details_3 = {"username":"janet", "email": 98745, "password":12345}
		response_ = self.checker.post('/api/v1/login', data=json.dumps(details_3), content_type = 'application/json')
		output_3 = json.loads(response_3.data)
		self.assertEqual(response_3, 200)
		self.assertEqual(output_3, "Please use data in string format for email")

		details_4 = {"username": "janet", "email": "janetnim401@gmail.com", "password": "schrodinger"}
		response_4 = self.checker.post('/api/v1/login', data=json.dumps(details_4), content_type = 'application/json')
		output_4 = json.loads(response_4.data)
		self.assertEqual(response_4, 200)
		self.assertEqual(output_4, "Please use data in int format for password")

	def test_user_log_in(self):
		# testing user log in entries -post
		details = {"username":"janet", "password": 12345}
		response = self.checker.post('/api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		details_1 = {"username":" ", "password":" "}
		response_1 = self.checker.post('/api/v1/login', data=json.dumps(details_1), content_type = 'application/json')
		output_1 = json.loads(response_1.data)
		self.assertEqual(response_1, 200)
		self.assertEqual(output_1, "Can not log in! Please enter all details")

		details_2 = {"username":5252, "password": 12345}
		response_2 = self.checker.post('/api/v1/login', data=json.dumps(details_2), content_type = 'application/json')
		output_2 = json.loads(response_2.data)
		self.assertEqual(response_2, 200)
		self.assertEqual(output_2, "Please use data in string format for username")

		details_3 = {"username":"janet", "password":"12345"}
		response_3 = self.checker.post('/api/v1/login', data=json.dumps(details_3), content_type = 'application/json')
		output_3 = json.loads(response_3.data)
		self.assertEqual(response_3, 200)
		self.assertEqual(output_3, "Please use data in integer format for password")

	def test_user_make_request(self):
		# testing user make a request -post
		request_data = {"request_id": "1234", "request": "bulb repair", "department": "HR"}
		response = self.checker.post("/api/v1/request", data=json.dumps(request_data), content_type= 'application/json')
		self.assertEqual(response.status_code, 200)

		details = {"username":"janet", "password":"12345"}
		response = self.checker.post('/api/v1/login', data=json.dumps(details), content_type = 'application/json')

		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		make_request = json.dumps(request_data)
		response = self.checker.post("/api/v1/makerequest", data=make_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)


	def test_user_view_a_request(self):
		# testing user viewing each request -get
		request_data = {{"request_id":1234} : {"request":"clock repair"}}
		response = self.checker.post('/api/v1/request/', data=json.dumps(request), content_type = 'application/json')
		output= json.loads(response.data)

		details = {"username":"janet", "password":"12345"}
		response = self.checker.post('/api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		view_request = json.dumps(request_data)
		response = self.checker.get("api/v1/view/1234", data=view_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)


	def test_user_view_all_requests(self):
		# testing user view all his requests -get
		details = {"username":"janet", "password":"12345"}
		response = self.checker.post('api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		all_requests = {{"request_id":1234, "request":"clock repair"}, {"request_id":4567, "request":"door repair"},{"request_id":7896,"request_id":1234}}
		response = self.checker.get('api/v1/view/', data=json.dumps(all_requests), content_type = 'application/json')
		output = json.loads(response.data)

	def test_modify_request(self):
		# testing user modify a request, after being able to log in -update
		request_data= {"request_id":1234, "request":"clock repair"}
		response = self.checker.post('api/v1/request', data=json.dumps(request_data), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

		details = {"username":"janet", "password":"12345"}
		response = self.checker.post('api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		make_request = json.dumps(request_data)
		response = self.checker.post("api/v1/make_request", data=make_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)

		modify_request = json.dumps({"request":"door repair"})
		response = self.checker.put('api/v1/modify/1234', data=modify_request, content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

	def test_delete_a_request(self):
		# testing a user delete a request after logging in   and making the request - delete
		request_data = {"request_id":1234, "request":"clock repair"}
		response = self.checker.post('api/v1/request', data=json.dumps(request_data), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

		details = {"username":"janet", "password":"12345"}
		response = self.checker.post('api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		make_request = json.dumps(request_data)
		response = self.checker.post("api/v1/make_request", data=make_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)
		
		view_request = json.dumps(request_data)
		response = self.checker.get("api/v1/view/1234", data=view_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)

		delete_request = json.dumps(request_data)
		response = self.checker.delete('api/v1/delete/1234', data=delete_request, content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

	def test_user_gets_feedback(self):
		# testing the user getting feedback from admin - get
		request_data = {"request_id":1234, "request":"clock repair"}
		response = self.checker.post('api/v1/request', data=json.dumps(request_data), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

		details = {"username":"janet", "password":"12345"}
		response = self.checker.post('api/v1/login', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		make_request = json.dumps(request_data)
		response = self.checker.post("api/v1/make_request", data=make_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)

		view_request = json.dumps(request_data)
		response = self.checker.get("api/v1/view/1234", data=view_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)

		get_feedback = json.dumps(request_data)
		response = checker.get('api/v1/feedback', data=get_feedback, content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

class Admin(unittest.TestCase):
	def test_admin_logs_in(self):
		# testing admin logging in - post
		details = {"username":"elidy", "password":"454545"}
		response = self.checker.post('api/v1/adminlogin', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		details_2 = {"username":54875, "password":"129945"}
		response_2 = self.checker.post('api/v1/adminlogin', data=json.dumps(details2), content_type = 'application/json')
		output_2 = json.loads(response2.data)
		self.assertEqual(response_2, 200)
		self.assertEqual(output_2, "Please use data in string format")

	def test_admin_should_view_requests(self):
		# testing admin viewing all requests - get
		request_data = {"request_id":1234, "request":"clock repair", "status":"completed"}
		response = self.checker.post('api/v1/request', data=json.dumps(request_data), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

		view_request = json.dumps(request_data)
		response = self.checker.get("api/v1/view/1234", data=view_request, content_type= 'application/json')
		self.assertEqual(response.status_code, 200)

	def test_admin_should_resolve_requests(self):
		# testing admin resolve requests and update status - update
		request_data = {"request_id":1234, "request":"clock repair", "status":"inomplete"}
		response = self.checker.post('api/v1/request', data=json.dumps(request_data), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

		details = {"username":"elidy", "password":"454545"}
		response = self.checker.post('api/v1/adminlogin', data=json.dumps(details), content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, "You have successfully logged in")

		resolve_request = json.dumps({"status" : "completed"})
		response = self.checker.put('api/resolve_requests/1234', data=modify_request, content_type = 'application/json')
		self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
	unittest.main()
