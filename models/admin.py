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
        '''checks each request sent'''
        request1 = [
            request1 for request1 in Admin().received_requests if request1["request_id"] == request_id]
        for request in request1:
            return "Request is present"
        if len(request1) == 0:
            return "No request present"

    def view_all_requests(self):
    	#fetchs all requests sent to admin
    	if len(Admin().received_requests) == 0:
    		return "No received requests available"
    	return "Requests available"

    def resolve_requests(self, request_id, request, department):
    	#fetches request info for the admin to resolve
    	if request_id == "" or request == "" or department == "":
    		return "No request present"
    	request2 = [
            request1 for request1 in Admin().received_requests if request1["request_id"] == request_id]
    	if not request2:
    		return "No request present, you cannot resolve"
    	return "Request is present, you can resolve"
          			                          
          			                          