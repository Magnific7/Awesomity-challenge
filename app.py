from flask import Blueprint
from flask_restful import Api

from resources.Hello import Hello
from resources.Employees import AllEmployees, EmployeeByEmail, EmployeeByPhonenumber, EmployeeByPosition, EmployeeByName, EmployeeActivate, EmployeeSuspend, EmployeeDelete, EmployeeEdit
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Hello, '/')
#route to see all employees
api.add_resource(AllEmployees, '/employees')
#route to search by email
api.add_resource(EmployeeByEmail, '/employees/email/<string:keyword>')
#route to search by postition
api.add_resource(EmployeeByPosition, '/employees/position/<string:keyword>')
#route to search by name
api.add_resource(EmployeeByName, '/employees/name/<string:keyword>')
#route to search by phonenumber
api.add_resource(EmployeeByPhonenumber, '/employees/phone/<string:keyword>')
#route to activate an employee
api.add_resource(EmployeeActivate, '/employees/<int:id>/activate')
#route to suspend an employee
api.add_resource(EmployeeSuspend, '/employees/<int:id>/suspend')
#route to 3dit employee credentials
api.add_resource(EmployeeEdit, '/employees/<int:id>')
#route to 3dit employee credentials
api.add_resource(EmployeeDelete, '/employees/<int:id>')





