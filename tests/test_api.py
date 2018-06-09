import unittest
import run

class TestModels(unittest.TestCase):
    """Test models for verion 2 api"""

    def setUp(self):
    	self.checker = app.test_client()

    def test_user_signup(self):
    	pass
    def test_user_login(self):
    	pass
    def test_user_make_request(self):
    	res = self.checker().post('/', data = )
    	self.assertEqual(res.status_code, 201)
    	self.assertIn("data info here", str(res.data))

    def test_user_view_a_request(self):
    	res = self.checker().post('/', data=)
    	self.assertEqual(res.status_code, 201)
    	response = json.loads(res.data.decode('utf-8').replace)
    	res2 = self.checker().get('/'.format(response[request_id]))
    	self.assertEqual(result.status_code, 200)
    	self.assertIn('data', str(res2.data))

    def test_user_view_all_requests(self):
    	res = self.checker().post('/', data=)
    	self.assertEqual(res.status_code, 201)
    	res = self.checker().get('/')
    	self.assertEqual(res.status_code, 200)
    	self.assertIn("data here", str(res.data))

    def test_user_modify_a_request(self):
    	pass
    def test_user_delete_a_request(self):
    	pass
    def test_admin_view_requests(self):
    	data = request.json.get
    	pass
    def test_admin_approve_request(self):
    	pass
    def test_admin_reject_request(self):
    	pass
    def test_admin_resolve_request(self):
    	pass
    def test_admin_delete_request(self):
    	pass