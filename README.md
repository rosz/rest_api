# rest_api
REST API based on Tornado framework

A project provides 5 methods:

* POST/add --> receives JSON, returns a summary of given numbers
* POST/multiply --> receives JSON, returns a multplication of given numbers
* PUT/memory --> saves numbers, returns "status" : "ok"
* GET/memory --> returns all numbers from the data base
* DELETE/memory --> deletes all numbers from the database, returns "status" : "ok"
* Unit tests included
