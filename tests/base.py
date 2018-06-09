import test_models.py

class BaseCase(object):
	def setUp(self):
		self.user={
			"personal_id": 1
			"username":"janet",
			"email":"janetnim401@gmail.com",
			"password": "4587L"

		}
		self.request={
			"request_id": 1,
			"request": "chair repair",
			"department": "hr",
			"personal_id": 1
		}
		