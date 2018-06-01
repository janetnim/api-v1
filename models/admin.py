from .user import User
class Admin(object):

    admin = {'username': 'admin', 'password': 121212}
    received_requests = []

    def __init__(self):
        self.results = {}

    def received_request(self):
        '''checks requests sent by each user'''
        Admin().received_requests.append(User().request_data)        
        res = Admin().received_requests
        return res

    # def resolve_requests(self, request_id):
    # 	'''fetches request info for the admin to resolve'''
    # 	Admin().received_requests.append(User().request_data)
    # 	request2 = [
    #         request1 for request1 in Admin().received_requests if request1["request_id"] == request_id]
    # 	if request2:
    # 		return "Request is present, you can resolve"
    # 	return "No request present, you cannot resolve"
    	
          			                          
          			                          