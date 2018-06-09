[![Build Status](https://travis-ci.org/janetnim/api-v1.svg?branch=develop)](https://travis-ci.org/janetnim/api-v1)
[![Coverage Status](https://coveralls.io/repos/github/janetnim/api-v1/badge.svg?branch=ft-api-test)](https://coveralls.io/github/janetnim/api-v1?branch=ft-api-test) 
# Maintenance Tracker Api V2
This is the API version 2 repository for the maintenance tracker application.

## Description
In challenge 3, we are required to first create a test for the API endpoints. The tests should first fail since no apis have been provided for the test. We are required to use token based authentication with JSON tokens for the log in endpoint as well as apply necessary security in required endpoints. We will use database to store the user and requests information in tables as well as querry our database. The APIs d]should be documented and hostedon heroku after passing build on travis and testing coverage.

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

## Endpoints to be covered
User can sisign up, login in and log out
The user can fetch a request he made
The user can fetch all the requests he made
The user can modify a request but not if it is approved by the admin
The user can delete a request
An admin can view all requests
An admin can approve, reject or resolve a request
An admin can delete a specific request

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
git checkout develop2
```

Ensure you have downloaded postgresql database and connected
```
pip install postgresql
\connect maintenance
```


## Links
[Github](https://github.com/janetnim/api-v1.git)
[Medium post](https://medium.com/@janetnim401/boot-camp-week-1-bf4f288da644)
[Pivotal tracker stories](https://www.pivotaltracker.com/n/projects/2173438)
[Pull request](https://github.com/janetnim/api-v1/pull/2)
(https://github.com/janetnim/api-v1/compare/develop2...ft-api-v2-test?expand=1)
