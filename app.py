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
#route to seaarch by email
api.add_resource(EmployeeByEmail, '/Employees/email/<string:keyword>')
api.add_resource(EmployeeByPosition, '/Employees/position/<string:keyword>')
api.add_resource(EmployeeByName, '/Employees/name/<string:keyword>')
api.add_resource(EmployeeByPhonenumber, '/Employees/phone/<int:id>')
api.add_resource(EmployeeByPhonenumber, '/Employees/phone/<int:id>')



