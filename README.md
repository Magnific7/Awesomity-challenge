# Awesomity-challenge

### My name is UWIKUZO Marie Magnificat
#### I am a fullstack web deloper applying at awesomity and this an entry challenge for backend.

## Employee management REST API (Back-End)
#### User experience expected
* A manager should be able to create an employee bypassing the below details to the API (employee name, national id, phone number, email, date of birth, status(active, inactive) and position(manager, developer, designer, etc...). After creating the employee, the system should send a communication email to the uploaded employees informing, they joined the company with the company name.ROUTE: /employees (REQUEST: POST)
* A manager should be able to edit, suspend, activate, and delete employee records.
* Delete Employee ROUTE: /employees/{employee id} (REQUEST: DELETE)
* Edit Employee ROUTE: /employees/{employee id} (REQUEST: PUT)
* Activate Employee ROUTE: /employees/{employee id}/activate (REQUEST: PUT)
* Suspend Employee ROUTE: /employees/{employee id}/suspend (REQUEST: PUT)
* Search Feature:
######A manager should be able to search for an employee based on his position, name, email or phone number.
######>Search ROUTE: /employees/search (REQUEST: POST)

### Prerequisites
You need the following to start working on the project on your local computer:

A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:
* Python version 3.6
* Flask
* Pip
* virtualenv
* text  Editor
* Postman

### Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.
* Install all packages by running " pip install -r requirements.txt"

### Technologies Used
*Python v3.6
* Flask

### License
MIT License

Copyright (c) 2019 UM MAGNIFIC
