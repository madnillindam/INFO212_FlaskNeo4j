from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

# KLASSER
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_Username(self):
        return self.username

    def set_Username(self, value):
        self.username = value

    def get_Email(self):
        return self.email

    def set_Email(self, value):
        self.email = value

class Car:
    def __init__(self, make, model, car_id, year, location, car_state):
        self.make = make
        self.model = model
        self.car_id = car_id
        self.year = year
        self.location = location
        self.car_state = car_state

    def get_make(self):
        return self.make 

    def set_make(self, value):
        self.make = value

    def get_model(self):
        return self.model 

    def set_model(self, value):
        self.model = value

    def get_car_id(self):
        return self.car_id

    def set_car_id(self, value):
        self.car_id = value

    def get_year(self):
        return self.year

    def set_year(self, value):
        self.year = value
    
    def get_location(self):
        return self.location

    def set_location(self, value):
        self.location = value
    
    def get_car_state(self):
        return self.car_state

    def set_car_state(self, value):
        self.car_state = value

class Customer:
    def __init__(self, customer_id, name, email, age=None, address=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.age = age
        self.address = address

    def get_id(self):
        return self.customer_id 

    def set_customer_id(self, value):
        self.customer_id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value
    
class Employee:
    def __init__(self, emp_id, name, address, branch):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.branch = branch

    def get_name(self):
        return self.name

    def set_email(self, value):
        self.email = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value
    
    def get_branch(self):
        return self.age

    def set_age(self, value):
        self.branch = value
