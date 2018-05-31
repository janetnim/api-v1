import unittest
from models.admin import Admin 
from models.user import User

class TestModels(unittest.TestCase):
	"""Test models for verion 1 api"""
	def test_sign_up_empty(self):
		results = User().sign_up("", "email@email.com", 3456)
		self.assertEqual(results, "Error! You have blank entries")

	def test_sign_up_user_enters_wrong_value(self):
		results = User().sign_up(2145, "janetnim401@gmail.com", 3555)
		self.assertEqual(results, "Enter a string value for name and email and integer value for password")

	def test_if_user_already_exists(self):
		results = User().sign_up("janet", "janetnim401@gmail.com", 66555)
		self.assertEqual(results, "user already exists")

	def test_user_successfully_signed_up(self):
		results = User().sign_up("kiki", "kikinim401@gmail.com", 68696)
		self.assertEqual(results, "You have succcessfully been registered!")

	def test_login_user(self):
		results = User().login("", 3456)
		self.assertEqual(results, "Error! please enter all details")

	def test_successful_log_in(self):
		results = User().login("janet", 66555)
		self.assertEqual(results, "You have succcessfully logged_in")

	def test_user_make_an_empty_request(self):
		results = User().make_request(" ","bulb repair", "hr")
		self.assertEqual(results, "Error! Please fill all the details")

	def test_user_make_request_with_id_present(self):
		results = User().make_request(1234, "bulb repair", "hr")
		self.assertEqual(results, "Invalid request id")

	def test_user_successful_make_request(self):
		results = User().make_request("90210","closet repair", "procurement")
		self.assertEqual(results, "Successfully made a request")

	def test_user_view_non_nexisting_request(self):
		results = User().make_request(101010)
		self.assertEqual(results, "Request not present")
	
	def test_user_view_existing_request(self):
		results = User().make_request("90210","closet repair", "procurement")
		self.assertEqual(results,"Request is present")
	
	def test_user_view_non_existing_requests(self):
		results = User().make_request()
		self.assertEqual(results, "No requests available")
	
	def test_user_modify_non_existing_request(self):
		results = User().make_request()
		self.assertEqual(results, "Error! request does not exist")

	def test_user_modify_existing_request(self):
		results = User().make_request(1234)
		self.assertEqual(results, "Changes Successfully made")

	def test_user_delete_non_existing_request(self):
		results = User().make_request(3333)
		self.assertEqual(results, "Error! the request does not exist")

	def test_user_delete_existing_request(self):
		results = User().make_request(1234)
		self.assertEqual(results, "Request successfully deleted")

if __name__ == '__main__':
	unittest.main()