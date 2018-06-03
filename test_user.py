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
        self.assertEqual(
            results, "Enter a string value for name and email and integer value for password")

    def test_if_user_already_exists(self):
        results = User().sign_up("janet", "janetnim401@gmail.com", 66555)
        self.assertEqual(results, "user already exists")

    def test_user_successfully_signed_up(self):
        results = User().sign_up("kiki", "kikinim401@gmail.com", 68696)
        self.assertEqual(results, "You have successfully been registered!")

    def test_login_user(self):
        results = User().login("", 3456)
        self.assertEqual(results, "Error! please enter all details")

    def test_successful_log_in(self):
        results = User().login("janet", 66555)
        self.assertEqual(results, "You have successfully logged_in")
        
    def test_log_in_unexisting_account(self):
    	results = User().login("Kendall", 4010)
    	self.assertEqual(results, "Your account does not exist, please sign sign_up")

    def test_user_make_an_empty_request(self):
        results = User().make_request(2323, "", "")
        self.assertEqual(results, "Error! Please fill all the details")

    def test_user_make_request_with_existing_id(self):
        results = User().make_request(5478, "bulb repair", "hr")
        self.assertEqual(results, "Invalid request id")

    def test_user_successful_make_request(self):
        results = User().make_request(90210, "closet repair", "procurement")
        self.assertEqual(results, "Successfully made a request")

    def test_user_view_non_nexisting_request(self):
        results = User().view_a_request(101010)
        self.assertEqual(results, "Request not present")

    def test_user_view_existing_request(self):
        results = User().view_a_request(5478)
        self.assertEqual(results, "Request is present")

    # def test_user_views_all_requests(self):
    # 	results = User().view_all_requests()
    # 	self.assertIsInstance(results, list, msg='Incorrect output type')

    def test_user_modify_non_existing_request(self):
        results = User().delete_request(4000)
        self.assertEqual(results, "Error! The request does not exist")

    def test_user_modify_existing_request(self):
        results = User().modify_request(5478, 'vehicle maintenance')
        self.assertEqual(results, "Changes successfully made")

    def test_user_delete_non_existing_request(self):
        results = User().delete_request(3333)
        self.assertEqual(results, "Error! The request does not exist")

    def test_user_delete_existing_request(self):
        results = User().delete_request(5555)
        self.assertEqual(results, "Request successfully deleted")


if __name__ == '__main__':
    unittest.main()
