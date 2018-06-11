import unittest
import json
from run import create_app
from helper import helper


class TestModels(unittest.TestCase):
    """Test models for verion 2 api"""

    def setUp(self):
        # self.app = create_app()
        self.checker = create_app("TESTING").test_client()
        self.request = {"request":"bulb repair","department":"hr", "status": "Pending"}
        self.user = {"username": "kenny", "email": "kenny@gmail.com", "password": "kenny254"}
        self.header = {"Content-Type": "application/json"}
        self.loggedInUserHeaders = {"Content-Type": "application/json"}
        self.loggedInAdminHeaders = {"Content-Type": "application/json"}

        self.logged_user = {"username": "peter", "email": "peter@users.com", "password": "who_cares"}

        res = self.checker.post('/api/v2/auth/signup', data=json.dumps(self.logged_user), headers=self.header)
        login_res = self.checker.post('/api/v2/auth/login', data=json.dumps(self.logged_user), headers=self.header)
        result = json.loads(login_res.data.decode())
        self.loggedInUserHeaders['Authorization'] = "Bearer {}".format(result['token'])

        self.logged_admin = {"username": "admin", "email": "admin@gmail.com", "password": "admin254"}
        login_rv = self.checker.post('/api/v2/auth/login', data=json.dumps(self.logged_admin), headers=self.header)
        result = json.loads(login_rv.data.decode())

        self.loggedInAdminHeaders['Authorization'] = "Bearer {}".format(result['token'])

    def sign_up_user(self):
        data = self.user
        res = self.checker.post('/api/v2/auth/signup', data=json.dumps(data), headers=self.header)

    def test_api_signup(self):
        data = self.user
        res = self.checker.post('/api/v2/auth/signup', data=json.dumps(data), headers=self.header)

        result = json.loads(res.get_data(as_text=True))

        self.assertEqual(result['message'], "User successfully signed up")
        self.assertEqual(res.status_code, 201)

    def test_user_already_exists(self):
        '''Test user cannot be registered twice'''
        self.sign_up_user()
        res2 = self.checker.post('/api/v2/auth/signup', data=json.dumps(self.user), headers=self.header)
        self.assertEqual(res2.status_code, 202)
        # getting results in json format
        result = json.loads(res2.data.decode())
        self.assertEqual(result['message'], 'The user already exists')

    def test_api_login(self):
        self.sign_up_user()

        login_res = self.checker.post('/api/v2/auth/login', data=json.dumps(self.user), headers=self.header)
        #get result in json format
        result = json.loads(login_res.data.decode())
        print(result)
        self.assertEqual(result['message'], "You have logged in successfully")
        self.assertEqual(login_res.status_code, 200)

    def test_non_registered_user_login(self):
        none_user = {'email': 'jwan', 'password': 'jwan254'}
        res = self.checker.post('/api/v2/auth/login', data=json.dumps(none_user), headers=self.header)
        result = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 404)
        self.assertEqual(result['message'], "user not found")

    def test_empty_login_details(self):
        user = {'username': "", 'password': ""}
        res = self.checker.post('/api/v2/auth/login', data=json.dumps(user), headers=self.header)
        result = json.loads(res.data.decode())
        self.assertEqual(result['message'], "user not found")

    def test_api_user_make_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 201)

        result = json.loads(res.data.decode())
        self.assertEqual(result['message'], "request made successfully")

    def test_make_empty_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps({"request": "", "department":"", "status":"Pending"}), headers=self.loggedInUserHeaders)
        result = json.loads(res.data.decode())
        self.assertEqual(result['message'], "Please fill all details")

    def test_api_user_view_a_request(self):
        rv = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        self.assertEqual(rv.status_code, 201)

        response = json.loads(rv.data.decode())
        res = self.checker.get('/api/v2/users/requests/1', headers=self.loggedInUserHeaders)

        self.assertEqual(res.status_code, 200)

    def test_view_inexisting_request(self):
        rv = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        self.assertEqual(rv.status_code, 201)

        response = json.loads(rv.data.decode())
        res = self.checker.get('/api/v2/users/requests/10', headers=self.loggedInUserHeaders)

        self.assertEqual(res.status_code, 404)

    def test_api_user_view_all_requests(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 201)

        res = self.checker.get('/api/v2/users/requests', headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)

    def test_api_user_modify_a_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 201)

        response = json.loads(res.data.decode())

        request_id = response['request_id']

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)

        rv = self.checker.put('/api/v2/users/requests/{}'.format(request_id), data=json.dumps({"request": "container repair"}), headers=self.loggedInUserHeaders)
        self.assertEqual(rv.status_code, 200)

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)


    def test_api_user_delete_a_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 201)

        response = json.loads(res.data.decode())

        request_id = response['request_id']

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)

        res = self.checker.delete('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)
        #testing to see if the deleted request exists
        req = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(req.status_code, 404)

    def test_api_admin_view_requests(self):
        res = self.checker.get('/api/v2/users/requests', headers=self.loggedInAdminHeaders)
        self.assertEqual(res.status_code, 200)

    def test_admin_approve_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        request_id = json.loads(res.data.decode())['request_id']

        res = self.checker.get('/api/v2/requests/{}'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(res.status_code, 200)

        rv = self.checker.put('/api/v2/requests/{}/approve'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(rv.status_code, 200)

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)

        result = json.loads(res.data.decode())['res']
        self.assertEqual(result['status'], "Approve")

    def test_admin_reject_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        request_id = json.loads(res.data.decode())['request_id']

        res = self.checker.get('/api/v2/requests/{}'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(res.status_code, 200)

        rv = self.checker.put('/api/v2/requests/{}/disapprove'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(rv.status_code, 200)

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)

        result = json.loads(res.data.decode())['res']
        self.assertEqual(result['status'], "Disapprove")

    def test_admin_resolve_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        request_id = json.loads(res.data.decode())['request_id']

        res = self.checker.get('/api/v2/requests/{}'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(res.status_code, 200)

        rv = self.checker.put('/api/v2/requests/{}/resolve'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(rv.status_code, 200)

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 200)

        result = json.loads(res.data.decode())['res']
        self.assertEqual(result['status'], "Resolved")

    def test_admin_delete_request(self):
        res = self.checker.post('/api/v2/users/requests', data=json.dumps(self.request), headers=self.loggedInUserHeaders)
        request_id = json.loads(res.data.decode())['request_id']

        res = self.checker.get('/api/v2/requests/{}'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(res.status_code, 200)

        rv = self.checker.delete('/api/v2/requests/{}/delete'.format(request_id), headers=self.loggedInAdminHeaders)
        self.assertEqual(rv.status_code, 200)

        res = self.checker.get('/api/v2/users/requests/{}'.format(request_id), headers=self.loggedInUserHeaders)
        self.assertEqual(res.status_code, 404)

    def tearDown(self):
        helper.drop_everything()

if __name__ == '__main__':
    unittest.main()