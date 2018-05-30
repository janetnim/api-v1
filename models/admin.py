from user import User

class Admin(object):
	admin = {'username': 'admin', 'password': 121212}
	received_requests = [{
	'request_id': 1234,
	'request': 'Bulb repairs'
	'department': 'hr'
},{
	'request_id': 5478,
	'request': 'Window repair'
	'department': 'hr'
},{
	'request_id': 5555,
	'request': 'computer repairs'
	'department': 'hr'
}]

	def received_requests(self, received_requests):
		'''checks each request sent'''
		request1 = [request1 for request1 in received_requests if request1[request_id] == request_id]
		request1 = request1.split(",")
		for request in request1:
			return request

	def view_all_requests(self, received_requests):
		'''checks for existence of requests sent first'''
		received_requests = received_requests.split(",")
		if len(received_requests) == 0:
			return "No received requests available"
		return received_requests

	def resolve_requests(self, received_requests):
		