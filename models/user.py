from .admin import  Admin

class User(object):

    user = [{'username': 'janet', 'email': 'janetnim401@gmail.com', 'password': 66555}, {'username': 'kate', 'email': 'kate@gmail.com','password': 999454}, {'username': 'admin', 'email': 'admin@gmail.com', "password": 121212}]
    request_data = request_data = [{
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
        self.result = {}

    def sign_up(self, username, email, password):
        '''checking for details of the new user'''
        if username == "" or email == "" or password == "":
            return "Error! You have blank entries"

        if not isinstance(username, str)or not isinstance(email, str) or not isinstance(password, int):
            return "Enter a string value for name and email and integer value for password"

        '''checks if the user alreay exists'''
        user1 = [user1 for user1 in User().user if user1["username"] == username
                 and user1["email"] == email and user1["password"] == password]
        if user1:
            return "user already exists"

        self.result[username] = username
        self.result[email] = email
        self.result[password] = password
        User.user.append(self.result)
        return "You have succcessfully been registered!"

    def login(self, username, password):
        ''' validation that the user already exists'''
        if username == "" or password == "":
            return "Error! please enter all details"

        if not isinstance(username, str) or not isinstance(password, int):
            return "Enter a string value for uesername and integer value for password"

        user1 = [user1 for user1 in User().user if user1["username"] ==
                                                         username and user1["password"] == password]
        if user1 not in User().user["password"]:
            return "Your account does not exist, please sign sign_up"    
        return "You have successfully logged_in"

    def logout(self):
        session['logged_in'] == False
        if session["logged_in"] == False:
            return "logging out..."

    def make_request(self, request_id, request, department):
        '''checks if an empty request has been  entered or if it already exists'''
        if request_id == "" or request == "" or department == "":
            return "Error! Please fill all the details"
        request1 == [request1 for request1 in User(
        ).request_data if request1["request_id"] == request_id]
        if request1 in request_data:
            return "Invalid request id"
        
        self.result[request_id] = request_id
        self.result[request] = request
        self.result[department] = department
        Admin.received_requests.append(self.result)
        User.request_data.append(self.result)
        return "Successfully made a request"

    def view_a_request(self, request_id):
        '''fetches a specific user request using the request's id'''
        request1 = [request1 for request1 in User(
        ).request_data if request1["request_id"] == request_id]
        if request1 not in request_data:
            return "Request not present"
        return "Request is present"

    def view_all_requests(self):
        '''fetches all user requests if present'''
        request_data = request_data.split(",")
        if len(request_data) == 0:
            return "No requests available"
        return "Requests are available"

    def modify_request(self, request_id):
        '''checks for existence of a request by its id before modifying it'''
        request1 = [request1 for request1 in User(
        ).request_data if request1["request_id"] == request_id]
        if request1 not in request_data:
            return "Error! request does not exist"
        else:
            request = request_data["request"]
            result['request'] = 'vehicle maintenance'
        return 'Changes successfully made'

    def delete_request(self, request_id):
        '''checks for existence of a request by its id before deleting it'''
        request1 = [request1 for request1 in User(
        ).request_data if request1["request_id"] == request_id]
        if request1 not in request_data:
            return "Error! The request does not exist"
        User().request_data.remove(request1[0])
        Admin().received_requests.remove(request1[0])
        return "Request successfully deleted"
