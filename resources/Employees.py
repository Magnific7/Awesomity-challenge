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
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return{'message': 'No input data provided'}, 400
        #Validate and deserialize input

        data, errors = employee_schema.load(json_data)
        if errors:
            return errors, 422
        employees = Employees.query.filter_by(id=data['id']).first()
        if not employees:
            return {'message':'Employee does not exit'}, 400
            
        employees.name = data['name']
        employees.national_id = data['national_id']
        employees.phone_no = data['phone_no']
        employees.email = data['email']
        employees.dob = data['dob']
        employees.status = data['status']
        employees.position = data['position']
        db.session.commit()

        result = employee_schema.dump(employees).data
        return {'status':'success','data':result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message':'No input data provided'}, 400
        data, errors = employee_schema.load(json_data)
        if errors:
            return errors, 422
        employees = Employees.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = employee_schema.dump(employees).data
        
        return {'status':'success','data':result}, 204
