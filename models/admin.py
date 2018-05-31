class Admin(object):

    admin = {'username': 'admin', 'password': 121212}
    received_requests = [{
        'request_id': 1234,
        'request': 'Bulb repairs',
        'department': 'hr'
    }, {
        'request_id': 5478,
        'request': 'Window repair',
        'department': 'hr'
    }, {
        'request_id': 5555,
        'request': 'computer repairs',
        'department': 'hr'
    }]

    def __init__(self):
        self.results = {}

    def received_request(self, request_id, request, department):
        #checks each request sent
        request1 = [
            request1 for request1 in Admin().received_requests if request1["request_id"] == request_id]
        if request1:
        	return"Request is already present"

        self.result["request_id"] = request_id
        self.result["request"] = request
        self.result["department"] = department
        Admin().received_requests.append(self.result)
        return "Received a new request"

    def view_all_requests(self):
    	#fetchs all requests sent to admin
        return Admin().received_requests

    def resolve_requests(self, request_id):
    	#fetches request info for the admin to resolve
    	request2 = [
            request1 for request1 in Admin().received_requests if request1["request_id"] == request_id]
    	if not request2:
    		return "No request present, you cannot resolve"
    	return "Request is present, you can resolve"
          			                          
          			                          