import unittest
from models.user import User
from models.admin import Admin


class TestModels(unittest.TestCase):
    """Test models for verion 1 api"""
    def test_admin_receive_new_request(self):
    	results = Admin().received_request()
    	self.assertIsInstance(results, list, msg='Incorrect output type')

	  
if __name__ == '__main__':
    unittest.main()
