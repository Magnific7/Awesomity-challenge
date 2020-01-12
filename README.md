# Awesomity-challenge

### My name is UWIKUZO Marie Magnificat
#### I am a fullstack web deloper applying at awesomity and this an entry challenge for backend.

## Employee management REST API (Back-End)
#### User experience expected
* A manager should be able to create an employee bypassing the below details to the API (employee name, national id, phone number, email, date of birth, status(active, inactive) and position(manager, developer, designer, etc...). After creating the employee, the system should send a communication email to the uploaded employees informing, they joined the company with the company name.
>ROUTE: /employees (REQUEST: POST)
* A manager should be able to edit, suspend, activate, and delete employee records.
* Delete Employee ROUTE: /employees/{employee id} (REQUEST: DELETE)
* Edit Employee ROUTE: /employees/{employee id} (REQUEST: PUT)
* Activate Employee ROUTE: /employees/{employee id}/activate (REQUEST: PUT)
* Suspend Employee ROUTE: /employees/{employee id}/suspend (REQUEST: PUT)
* Search Feature:
######A manager should be able to search for an employee based on his position, name, email or phone number.
######>Search ROUTE: /employees/search (REQUEST: POST)
