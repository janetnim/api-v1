from admin import 

Class User(object):
	
	user = [{'username': 'janet', 'email':'janetnim401@gmail.com', 'password': 66555}, {'username': 'kate', 'email': 'kate@gmail.com', 'password': 66555}]
	request_data = request_data = [{
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

	def sign_up(self, username, email, password, result):
		'''checking for details of the new user'''
		if username == " " or email == " " or password == " ":
			return "Error! You have blank entries"

		if not isinstance(username, str)or not isinstance(email, str) or not isinstance(password, int):
			return "Enter a string value for name,email and integer value for password"

		'''checks if the user alreay exists'''
		user1 = [user1 for user1 in User().user if user1["username" == username] and user1["email"]==email and user1["password"] == password]
		if user:
			return "user already exists"
		result[username] = username
		result[email] = email
		result[password] = password
		User.user.append(result)
		return "You have succcessfully been registered!"

	def login(self, username, password):
		''' validation that the user already exists'''
		if username==" " or password == " ":
			return "Error! please enter all details"

		if not isinstance(username, str) or not isinstance(password, int):
			return "Enter a string value for uesername and integer value for password"

		user1 = [user1 for user1 in User().user if user1["username" == username] and user1["password"] == password]
		if user1 not in user:
			return "Your account does not exist, please sign sign_up"

	def logout(self):
		session['logged_in'] == False
		if session["logged_in"] == False:
			return "logging out..."

	def make_request(request_id, request, department, result):
		'''checks if an empty request has been  entered or if it already exists''' 
		if request_id == " " or request == " " or department == " ":
			return "Error! Please fill all the details"
		request1 == [request1 for request1 in User().request_data if request1["request_id"] == request_id]
		if request1 in request_data:
			return "Invalid request id"
		result[request_id] = request_id
		result[request] = request
		result[department] = department
		Admin.received_requests.append(result)
		User.request_data.append(result)

	def view_a_request():
		request1 = [request1 for request1 in User().request_data if request1["request_id"]==request_id]
		if request1 not in request_data:
			return "No such request present"
		return User().request_data([request1[0]])

	def view_all_requests():
		'''returns all requests if present'''
		request_data = request_data.split(",")
		if len(request_data) == 0:
			return "No requests made"
		return User().request_data

	def modify_request():
		'''checks for existnce of a request through its id before modifying it'''
		request1 = [request1 for request1 in User().request_data if request1["request_id"]==request_id]
		if request1 not in request_data:
			return "Error! request does not exist"
		else:
			request = request_data["request"]
			result['request'] = 'vehicle maintenance'
		return 'Changes made'

	def delete_request():
		'''checks for existence of a request through its id before deleting it'''
		request1 = [request1 for request1 in User().request_data if request1["request_id"]==request_id]
		if request1 not in request_data:
			return "Error! The request does not exist"
		Admin.received_requests.remove(request1[0])
		return "Request deleted"
