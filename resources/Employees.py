from flask import request
from flask_restful import Resource
from Model import db, Employees, EmployeesSchema

employees_schema = EmployeesSchema(many=True)
employee_schema = EmployeesSchema()

class AllEmployees(Resource):
    '''
    function to display all employees and there credentials.
    '''
    def get(self):
        employees = Employees.query.all()
        employees = employees_schema.dump(employees).data
        return {'status': 'success', 'data':employees},200
    '''
    fuction to add an employee and their credentials.
    '''
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return{'message': 'No input data provided'}, 400
        #Validate and deserialize input

        data, errors = employee_schema.load(json_data)
        if errors:
            return errors, 422
        employees = Employees.query.filter_by(name=data['name']).first()
        if employees:
            return {'message': 'Employee already exists'}, 400
        employees = Employees(
            name=json_data['name'],
            national_id = json_data['national_id'],
            phone_no = json_data['phone_no'],
            email = json_data['email'],
            dob = json_data['dob'],
            status = json_data['status'],
            position = json_data['position'],
        )
        db.session.add(employees)
        db.session.commit()

        result = employee_schema.dump(employees).data

        return {'status': 'success', 'data':result }, 201

class EmployeeEdit(Resource):
    '''
    function to edit employee's credentials .
    '''
    def put(self, id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        
        # Validate and deserialize input
        data, errors = employee_schema.load(json_data)
        if errors:
            return errors, 422

        employee = Employees.query.filter_by(id = id).first()
        if not employee:
            return {'message': 'Employee does not exist'}, 400

        employee.name = data['name']
        employee.national_id=data['national_id']
        employee.phone_no=data['phone_no']
        employee.email=data['email']
        employee.dob=data['dob']
        employee.status=data['status']
        employee.position=data['position']
        db.session.commit()

        result = employee_schema.dump(employee).data
        return {
            'status': 'success',
            'data': result
        }, 201

class EmployeeDelete(Resource):
    '''
    Function to delete an employee 's credentials
    '''
    def delete(self, id):
        employees = Employees.query.filter_by(id = id).delete()
        db.session.commit()

        result = employee_schema.dump(employees).data
        return {'status':'success','data':result}, 201

class EmployeeSuspend(Resource):
    '''
    Function to suspend  an employee
    '''
    def put(self, id):
        employees = Employees.query.filter_by(id = id).first()
        if not employees:
            return {'message':'Employee does not exit'}, 400

        employees.status = 'inactive'
        db.session.commit()

        result = employee_schema.dump(employees).data
        return {'status':'success','data':result}, 201

class EmployeeActivate(Resource):
    '''
    Function to active an employee.
    '''
    def put(self, id):
        employee = Employees.query.filter_by(id = id).first()
        if not employee:
            return {'message': 'Employee does not exist'}, 400

        employee.status="active"
        db.session.commit()

        result = employee_schema.dump(employee).data
        return {
            'status': 'success',
            'data': result
        }, 201


        ## These are the search functionalities
class EmployeeByName(Resource):
    '''
    function to search employee by their name
    '''
    def get(self, keyword):
        employee = Employees.query.filter(Employees.name.ilike(r"%{}%".format(keyword))).all()
        employee = employees_schema.dump(employee).data
        return {
            'status': 'success',
            'data': employee
        }, 200

class EmployeeByPosition(Resource):
    '''
    function to search employee by their position
    '''
    def get(self, keyword):
        employee = Employees.query.filter(Employees.position.ilike(r"%{}%".format(keyword))).all()
        employee = employees_schema.dump(employee).data
        return {
            'status': 'success',
            'data': employee
        }, 200

class EmployeeByEmail(Resource):
    '''
    function to search employee by their email
    '''
    def get(self, keyword):
        employee = Employees.query.filter(Employees.email.ilike(r"%{}%".format(keyword))).all()
        employee = employees_schema.dump(employee).data
        return {
            'status': 'success',
            'data': employee
        }, 200

class EmployeeByPhonenumber(Resource):
    '''
    function to search employee by their position
    '''
    def get(self, keyword):
        employee = Employees.query.filter(Employees.phone_no.ilike(r"%{}%".format(keyword))).all()
        employee = employees_schema.dump(employee).data
        return {
            'status': 'success',
            'data': employee
        }, 200