from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Employees(db.Model):
    __tablename_ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    national_id = db.Column(db.String(16), nullable=False)
    phone_no = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(250), nullable=False)
    dob = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, national_id, phone_no, email, dob, status, position):
        self.name = name
        self.national_id = national_id
        self.phone_no = phone_no
        self.email = email
        self.dob = dob
        self.status = status
        self.position = position

class EmployeesSchema(ma.Schema):
    id = fields.Integer(dump_only=True) 
    name = fields.String(required=True)
    national_id = fields.String(required=True)
    phone_no = fields.String(required=False)
    email = fields.String(required=True)
    dob = fields.Date()
    status = fields.String(required=True)
    position = fields.String(required=True)
    creation_date = fields.DateTime()