import unittest
from models.admin import Admin
from models.user import User


class TestModels(unittest.TestCase):
    """Test models for verion 1 api"""

    def test_admin_receive_existing_request(self):
        results = Admin().received_request(1234, "Bulb repairs", "hr")
        self.assertEqual(results, "Request is already present")

    def test_admin_receive_new_request(self):
        results = Admin().received_requests(1546, "Iron repair", "fianance")
        self.assertEqual(results, "Received a new request")

    def test_user_views_all_requests(self):
    	results = Admin().view_all_requests()
    	self.assertIsInstance(results, list, msg='Incorrect output type')

    def test_admin_resolve_request_exists(self):
        results = Admin().resolve_requests(1234)
        self.assertEqual(results, "Request is present, you can resolve")

    def test_admin_resolve_request_id_does_not_exist(self):
        results = Admin().resolve_requests(85878)
        self.assertEqual(
            results, "No request present, you cannot resolve")

	  
if __name__ == '__main__':
    unittest.main()
