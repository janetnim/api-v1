[![Build Status](https://travis-ci.org/janetnim/api-v1.svg?branch=ft-api-test)](https://travis-ci.org/janetnim/api-v1)
[![Coverage Status](https://coveralls.io/repos/github/janetnim/api-v1/badge.svg?branch=ft-api-test)](https://coveralls.io/github/janetnim/api-v1?branch=ft-api-test) 
# Maintenance Tracker Api V1
This is the API version 1 repository for the maintenance tracker application.

## Description
In challenge 2, we are required to first create a test for the API endpoints. The tests should first fail since no apis have been provided for the test. The four major tests for the endpoints are that a logged in user should be able to make a request, fetch a request, fetch all requests made by the user, modify  and delete a request. After writing the tests, you can now write the apis for the endpoints and check that they meet the tests written.

## Tasks to be done
The tasks to be completed for the event are: 
1. Write a unit test code for the api endpoints
2. Create endpoints for that satisfy the test created
3. Create a new repo for your apis and test
4. Update pivotal tracker stories
5. Create a medium blog post
6. Create a virtual environment for your application to run on
7. Test your code on postman, travis CI,
8. Update your readme and add badge

## Development
The Pivotal Tracker stories are located [here](https://www.pivotaltracker.com/n/projects/2173438)

Create a api-v1 repository on github and clone it with the command:
```
git clone https://github.com/janetnim/api-v1.git
```

In your terminal create a virtual environment and activate it:
```
virtualenv venv
. virtual/bin/activate
```

To intall dependancies
```
pip install -r requirements.txt
pip install flask
```

then checkout to develop branch and navigate to the api and test files in your local repository
```
git checkout develop
```

## Links
[Github](https://github.com/janetnim/api-v1.git)
[Medium post](https://medium.com/@janetnim401/team-dynamism-all-the-way-37b49c965a4a)
[Pivotal tracker stories](https://www.pivotaltracker.com/n/projects/2173438)
[Pull request](https://github.com/janetnim/api-v1/pull/1)
