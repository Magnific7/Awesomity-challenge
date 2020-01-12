from flask import Blueprint
from flask_restful import Api

from resources.Hello import Hello
from resources.Employees import AllEmployees, EmployeeByEmail, EmployeeByPhonenumber, EmployeeByPosition, EmployeeByName, EmployeeActivate, EmployeeSuspend, EmployeeDelete, EmployeeEdit
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Hello, '/')
#route to see all employees
api.add_resource(AllEmployees, '/Employees')
#route to search by email
api.add_resource(EmployeeByEmail, '/Employees/email/<string:keyword>')
#route to search by postition
api.add_resource(EmployeeByPosition, '/Employees/position/<string:keyword>')
#route to search by name
api.add_resource(EmployeeByName, '/Employees/name/<string:keyword>')
#route to search by phonenumber
api.add_resource(EmployeeByPhonenumber, '/Employees/phone/<int:id>')
#route to activate an employee
api.add_resource(EmployeeActivate, '/Employees/<int:id>/activate')
#route to suspend an employee
api.add_resource(EmployeeSuspend, '/Employees/<int:id>/suspend')
#route to 3dit employee credentials
api.add_resource(EmployeeEdit, '/Employees/<int:id>')
#route to 3dit employee credentials
api.add_resource(EmployeeDelete, '/Employees/<int:id>')





