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

