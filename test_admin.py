import unittest
from models.admin import Admin 
from models.user import User

class TestModels(unittest.TestCase):
    """Test models for verion 1 api"""
    def test_admin_receive_request(self):
        results = Admin().received_request("", "email@email.com", 3456)
        self.assertEqual(results, "Error! You have blank entries")