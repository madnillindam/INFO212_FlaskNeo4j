from click import make_pass_decorator
from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json
from project.models.User import User, Car, Customer, Employee
import re
import random

# CONNECT TO DB
URI = "neo4j+ssc://5b571bf5.databases.neo4j.io"
AUTH = ("neo4j", "7DnsYLOCMyRtpIU8i8kIe12l4X561YJPvophJyS5bgI")

def get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

#Print noder til terminal
def print_json(nodes):
        for i in nodes:
            print(f"Node: {i}")
        return nodes

### ENDPOINTS ###
   
### USERS ###
def findAllUsers():
    with get_connection().session() as session:
        users = session.run("MATCH(c:User) RETURN c;")
        nodes_json = [node_to_json(record["c"]) for record in users]
        # print(type(nodes_json))
        print_json(nodes_json)
        return nodes_json

# Returnerer e-post adresse for username
def findUserByUsername(username):
        data = get_connection().execute_query("MATCH (a:User) where a.username = $username RETURN a;", username=username)
        print()
        if len(data[0]) > 0:
            user = User(username, data[0][0][0]['email'])
            print("user: ", user)
            return user
        else:
            return User(username, "Not found in DB")

### CARS ###
def findAllCars():
    with get_connection().session() as session:
        cars = session.run("MATCH(c:Cars) RETURN c;")

        nodes_json = [node_to_json(record["c"]) for record in cars]
        print_json(nodes_json)
        return nodes_json
    
def findCarbyIdNumber(car_id):
    with get_connection().session() as session:
        cars = session.run("MATCH (c:Cars{car_id: $car_id}) return c;", car_id=car_id)
        print(type(cars))
        print(cars)
        nodes_json = [node_to_json(record["c"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
def save_car(make, model, car_id, year, location, car_state):
    with get_connection().session() as session: 
        cars = session.run("MERGE (c:Cars{make: $make, model: $model, car_id: $car_id, year: $year, location: $location, car_state: $car_state}) RETURN c;", 
                                           make=make, model=model, car_id=car_id, year=year, location=location, car_state=car_state)

        nodes_json = [node_to_json(record["c"]) for record in cars]
        print_json(nodes_json)
        return nodes_json

def update_car(make, model, car_id, year, location, car_state):
    with get_connection().session() as session: 
        cars = session.run("MATCH (c:Cars{car_id: $car_id}) SET c.make=$make, c.model=$model, c.car_id=$car_id, c.year=$year, c.location=$location, c.car_state=$car_state RETURN c;", 
                           make=make, model=model, car_id=car_id, year=year, location=location, car_state=car_state)

        nodes_json = [node_to_json(record["c"]) for record in cars]
        print_json(nodes_json)
        return nodes_json

# TODO Hvorfor .execute_query her istedenfor session.run som på de andre? 
# As is: TypeError: The view function for 'delete_car_info' did not return a valid response. The function either returned None or ended without a return statement.
def delete_car(car_id):
    # get_connection().execute_query("MATCH (c:Cars{car_id: $car_id}) Detach DELETE c", car_id=car_id)
    with get_connection().session() as session: 
        employees = session.run("MATCH (c:Cars{car_id: $car_id}) Detach DELETE c", car_id=car_id)

        nodes_json = [node_to_json(record["c"]) for record in employees]
        return print_json(nodes_json)

### CUSTOMERS - FUNKSJONER ###
# OK
def findAllCustomers():
    with get_connection().session() as session:
        customers = session.run("MATCH(c:Customer) RETURN c;")

        nodes_json = [node_to_json(record["c"]) for record in customers]
        print_json(nodes_json)
        return nodes_json 

# Virker! 
def findCustomerByName(name):
    data = get_connection().execute_query("MATCH (a:Customer) where a.name = $name RETURN a;", name=name)
    if len(data[0]) > 0:
        customer = Customer(data[0][0][0]['customer_id'], name, data[0][0][0]['email'])
        print("customer: ", customer)
        return customer
    else:
        return Customer(name, "Not found in DB")

# OK, json
def findCustomerbyIdNumber(customer_id):
    with get_connection().session() as session:
        customers = session.run("MATCH (c:Customer{customer_id: $customer_id}) return c;", customer_id=customer_id)
        
        nodes_json = [node_to_json(record["c"]) for record in customers]
        print(type(nodes_json))
        print_json(nodes_json)
        return nodes_json

# OK, json    
def save_customer(customer_id, name, email, age, address):
    with get_connection().session() as session: 
        customers = session.run("MERGE (c:Customer{customer_id: $customer_id, name: $name, email: $email, age: $age, address: $address}) RETURN c;", 
                                           customer_id=customer_id, name=name, email=email, age=age, address=address)

        nodes_json = [node_to_json(record["c"]) for record in customers]
        print_json(nodes_json)
        return nodes_json

# OK, json    
def update_customer(customer_id, name, email, age, address):
    with get_connection().session() as session: 
        customers = session.run("MATCH (c:Customer{customer_id: $customer_id}) SET c.customer_id=$customer_id, c.name=$name, c.email=$email, c.age=$age, c.address=$address RETURN c;", 
                                customer_id=customer_id, name=name, email=email, age=age, address=address)

        nodes_json = [node_to_json(record["c"]) for record in customers]
        print_json(nodes_json)
        return nodes_json

# TODO Virker ikke?!?????????
def delete_customer(customer_id):
    with get_connection().session() as session: 
        customers = session.run("MATCH (c:Customer{customer_id: $customer_id}) DETACH DELETE c;", customer_id=customer_id)

        nodes_json = [node_to_json(record["c"]) for record in customers]
        print_json(nodes_json)
        return nodes_json

### EMPLOYEES ###
# OK
def findAllEmployees():
    with get_connection().session() as session:
        employees = session.run("MATCH(c:Employee) RETURN c;")
        print(type(employees))
        print(employees)
        nodes_json = [node_to_json(record["c"]) for record in employees]
        print_json(nodes_json)
        return nodes_json

# OK
def findEmployeebyIdNumber(emp_id):
    with get_connection().session() as session:
        employees = session.run("MATCH (c:Employee{emp_id: $emp_id}) return c;", emp_id=emp_id)

        nodes_json = [node_to_json(record["c"]) for record in employees]
        print_json(nodes_json)
        return nodes_json

# OK
def save_employee(emp_id, name, address, branch):
    with get_connection().session() as session: 
        employees = session.run("MERGE (c:Employee{emp_id: $emp_id, name: $name, address: $address, branch: $branch}) RETURN c;", 
                                           emp_id = emp_id, name = name, address = address, branch = branch)

        nodes_json = [node_to_json(record["c"]) for record in employees]
        print_json(nodes_json)
        return nodes_json

# OK     
def update_employee(emp_id, name, address, branch):
    with get_connection().session() as session: 
        employees = session.run("MATCH (c:Employee{emp_id: $emp_id}) SET c.emp_id=$emp_id, c.name=$name, c.address=$address, c.branch=$branch RETURN c;", 
                                emp_id = emp_id, name = name, address = address, branch = branch)

        nodes_json = [node_to_json(record["c"]) for record in employees]
        print_json(nodes_json)
        return nodes_json
        
# OK
def delete_employee(emp_id, name, address, branch):
    with get_connection().session() as session: 
        employees = session.run("MATCH (c:Employee{emp_id: $emp_id}) DETACH DELETE c;", emp_id=emp_id, name=name, address=address, branch=branch)

        nodes_json = [node_to_json(record["c"]) for record in employees]
        print_json(nodes_json)
        return nodes_json

### ACTIONS ###



#FUNKSJONER TIL ORDERS#

#sjekk om bil er tilgjengelig
def check_availability(car_id):
   
    return(findCarbyIdNumber(car_id)[0]["car_state"])


#sjekk om kunde ikke allerede leier en bil 
def check_eligibility(customer_id):

    return(findCustomerbyIdNumber(customer_id)[0]["is_renting"])

#skulle kanskje hatt 100% sikkerhet for unike ordrenummer,men 89,9999% får duge
def generate_order_id():
    return(random.randint(100000,999999))

#sjekk om det finnes en ordre med den kunden og den bilen - returnerer en streng, siden vi ikke får lov til å returnere bl.a. bool og int 
def order_exists(car_id,customer_id):
    with get_connection().session() as session: 
        order = session.run("MATCH (n:Order) WHERE n.customer_id = $customer_id AND n.car_id= $car_id RETURN n",customer_id=customer_id,car_id=car_id)
        print(type(order))
        print(order)
        nodes_json = [node_to_json(record["n"]) for record in order]
        return(nodes_json)




# ORDER CAR

def make_order(car_id,customer_id):
    print("make order")
    #sjekk om forholdene ligger til rette
    if  check_availability(car_id) == "available" and check_eligibility(customer_id) == "no":

        with get_connection().session() as session:
            order_id = generate_order_id()
            order = session.run("CREATE (c:Order {order_id: $order_id, customer_id: $customer_id,car_id: $car_id}) RETURN c;",
                                order_id=order_id,customer_id=customer_id,car_id=car_id )
            nodes_json = ([node_to_json(record["c"]) for record in order])
            session.run("MATCH (a:Cars{car_id: $car_id}) SET a.car_state='booked'",car_id=car_id)
            return(nodes_json) 
    else:
        return ("Terribly sorry, but conditions aren't met")

# GET ALL ORDERS

def findAllOrders():
    with get_connection().session() as session:
        orders = session.run("MATCH(c:Order) RETURN c;")

        nodes_json = [node_to_json(record["c"]) for record in orders]
        print_json(nodes_json)
        return nodes_json 

# CANCEL ORDER CAR

#må taste inn både bilnummer og kundenummer, siden det er det oppgaven ber om. Funker nå
def cancel_order_car(car_id,customer_id):
    order = order_exists(car_id,customer_id)
    if len(order)>0:
        order_id = order[0]["order_id"]
        
        
        with get_connection().session() as session:
            session.run("MATCH (o:Order {order_id: $order_id}) DELETE o;",order_id=order_id)
            session.run("MATCH (a:Cars{car_id: $car_id}) SET a.car_state='available'",car_id=car_id)
            session.run("MATCH (c:Customer{customer_id: $customer_id}) SET c.is_renting='no'",customer_id=customer_id)
            print("order was cancelled")
            return("order was cancelled")
    else:
        return("no such order")
  
# RENT CAR

def rent_car(car_id,customer_id):

    return()

# RETURN CAR

def return_car(order_id):
    return()


#HJELPEFUNKSJONER

#gjør alle biler tilgjengelige



#opprett relasjon 
def make_relation():
    car_id=22
    customer_id=5000
    with get_connection().session() as session:
        session.run("MATCH (Cars {car_id: 4}), (Customer {customer_id: 60}) CREATE (Customer)-[:KRÆSJET]->(Cars)") 
        return 'relasjon opprettet'

#hent relasjoner (funkar inte)
def findAllRelations():
    print('første')
    with get_connection().session() as session:
        print('andre')
        relations = session.run("MATCH (a)-[r]-(c) RETURN *")
        print("RELATIONS TYPE:\n",type(relations))
        for record in relations:
            print('tredje')
            print(type(record)) 
            print(record)
            print(record[0])
            for i in record:
                print("ting:",i)

        nodes_json = [node_to_json(record[0]) for record in relations]
        print_json(nodes_json)
        return nodes_json

#sjekk om kunde inngår i relasjon
def check_relation():
    with get_connection().session() as session:
        session.run("MATCH (Cars {car_id: 4}), (Customer {customer_id: 60}) CREATE (Customer)-[:KRÆSJET]->(Cars)") 

#slett relasjon
def delete_relation():
        with get_connection().session() as session:
            session.run("")











   