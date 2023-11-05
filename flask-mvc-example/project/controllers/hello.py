from project import app
from flask import render_template, request, redirect, url_for
from project.models.my_dao_endpoints import findUserByUsername, findCustomerByName
from project.models.my_dao_endpoints import *



### USERS ###
# TODO kjører uten feil, men får ikke tak i data fra databasen
# Get user email by providing username
@app.route('/user', methods=["GET", "POST"])
def user():
    if request.method == "POST":
        username = request.form["username"]
        try:
            user = findUserByUsername(username)
            data = {
                "username": user.username,
                "email": user.email
            }
        except Exception as err:
            print (err)
    else:
        data = {
            "username": "Not specified",
            "email": "Not specified"
        }
    return render_template('index.html.j2', data=data)

# SHOW ALL USERS
@app.route("/get_users", methods=["GET"])
def query_users():
    return findAllUsers()

### CARS ###
# Get all cars - dette fungerer - viser JSON av alle bilene
@app.route("/get_cars", methods=["GET"])
def query_records():
    return findAllCars()

## TODO DETTE VIRKER IKKE får tilbake http://localhost:8000/get_car_by_id_number/?car_id=2, 
# ikke http://localhost:8000/get_car_by_id_number/2 og da fungerer ikke neste lenke/funksjon
# # Forsøk - søkeside for å generere url for get_cars_by_id_number
# @app.route("/get_car_by_id_number/", methods=["GET"])
# def search_car_by_id():
#     return render_template("search.html.j2")

# Find car object by ID_number
# TODO Denne kjører nå, men mangler template
@app.route("/get_car_by_id_number/<int:car_id>", methods=["GET"])          # OBS typeangivelse må være med
def find_car_by_id_number(car_id):
    # record = json.loads(request.data)
    # print(record)
    # print(record["car_id"])
    
    return findCarbyIdNumber(car_id)

# Save (match/create) car
# TODO Denne kjører, men mangler template
# Adresse: http://localhost:8000/save_car?make=Skoda&model=Octavia&car_id=66&year=1980&location=Russland&car_state=booked
# OBS alle parameter må med.
@app.route("/save_car", methods=["GET"])         
def save_car_info():
    # record = json.loads(request.data)
    # print(record)

    url_params= request.args

    make = url_params.get("make")
    model = url_params.get("model")
    car_id = int(url_params.get("car_id"))
    year = int(url_params.get("year"))
    location = url_params.get("location")
    car_state = url_params.get("car_state")

    # return save_car(record["make"], record["model"], record["car_id"], record["year"], record["location"], record["car_state"])
    return save_car(make=make, model=model, car_id=car_id, year=year, location=location, car_state=car_state)

# Update car
# TODO virker, mangler template 
# http://localhost:8000/update_car?make=Toyota&model=Yaris&car_id=12&year=2001&location=%C3%85rstad&car_state=booked 
@app.route("/update_car", methods=["GET"])
def update_car_info():
    # record = json.loads(request.data)
    # print(record)
    # return update_car(record["make"], record["model"], record["car_id"], record["year"], record["location"], record["car_state"])
    url_params= request.args

    make = url_params.get("make")
    model = url_params.get("model")
    car_id = int(url_params.get("car_id"))
    year = int(url_params.get("year"))
    location = url_params.get("location")
    car_state = url_params.get("car_state")

    return update_car(make=make, model=model, car_id=car_id, year=year, location=location, car_state=car_state)

# Delete car
# OK
@app.route("/delete_car", methods=["GET"])
def delete_car_info():

    url_params= request.args

    car_id = int(url_params.get("car_id"))

    return delete_car(car_id=car_id)


### CUSTOMERS ###
# Get all customers - dette virker (returnerer json.)
@app.route("/get_customers", methods=["GET"])
def query_customers():
    return findAllCustomers()

# Get customer by ID (eller navn?)
# TODO Dette virker ikke
# UnboundLocalError: local variable 'data' referenced before assignment
@app.route('/customer', methods=["GET", "POST"])
def customer():
    if request.method == "POST":
        name = request.form["name"]
        # try:
        customer = findCustomerByName(name)
        data = {
            "name": customer.name, 
            "email": customer.email
            }
        # except Exception as err:
        #     print(err) 
    else:
        data = {
            "name": "Not specified",
            "email": "Not specified"
        }
    return render_template('customer.html.j2', data=data)

# Get customer by ID
# Returnerer json av en customer (http://localhost:8000/get_customer_by_id_number/2000)
@app.route("/get_customer_by_id_number/<int:customer_id>", methods=["GET"])          # OBS typeangivelse må være med
def find_customer_by_id_number(customer_id):
    return findCustomerbyIdNumber(customer_id)

# Create
# TODO Denne kjører, men mangler template
# Adresse: http://localhost:8000/save_customer?customer_id=28&name=KapteinSabeltann&email=hiv@hoi.com&age=88&address=Kristiansand
# # OBS alle parameter må med.
@app.route("/save_customer", methods=["GET"])         
def save_customer_info():

    url_params= request.args

    customer_id = int(url_params.get("customer_id"))
    name = url_params.get("name")
    email = url_params.get("email")
    age = int(url_params.get("age"))
    address = url_params.get("address")

    return save_customer(customer_id=customer_id, name=name, email=email, age=age, address=address)

# Update
#http://localhost:8000/update_customer?customer_id=28&name=KapteinSabeltann&email=hiv@hoi.com&age=88&address=Kjuttaviga
@app.route("/update_customer", methods=["GET"])         
def update_customer_info():

    url_params= request.args

    customer_id = int(url_params.get("customer_id"))
    name = url_params.get("name")
    email = url_params.get("email")
    age = int(url_params.get("age"))
    address = url_params.get("address")

    return update_customer(customer_id=customer_id, name=name, email=email, age=age, address=address)

# Delete
# http://localhost:8000/delete_customer?customer_id=60&name=SlettSlettesen&email=hav@hui.com&age=102&address=Oslo
# TODO
@app.route("/delete_customer", methods=["GET"])
def delete_customer():

    url_params= request.args

    customer_id = int(url_params.get("customer_id"))

    return delete_customer(customer_id=customer_id)


### EMPLOYEES ###
# Get all employees 
@app.route("/get_employees", methods=["GET"])
def query_employees():
    print("kjører query_employees")
    return findAllEmployees()

# Returnerer json av en customer (http://localhost:8000//get_employee_by_emp_id/2)
@app.route("/get_employee_by_emp_id/<int:emp_id>", methods=["GET"])          # OBS typeangivelse må være med
def find_employee_by_id_number(emp_id):
    return findEmployeebyIdNumber(emp_id)

# Create
# Adresse: http://localhost:8000/save_employee?emp_id=99&name=SharpShooter&address=WildWestTown&branch=Branc01
@app.route("/save_employee", methods=["GET"])         
def save_employee_info():

    url_params= request.args

    emp_id = int(url_params.get("emp_id"))
    name = url_params.get("name")
    address = url_params.get("address")
    branch = url_params.get("branch")


    return save_employee(emp_id = emp_id, name = name, address = address, branch = branch)

# Update
# http://localhost:8000/update_employee?emp_id=99&name=SharpShooter&address=WildWestTown&branch=Branch06
@app.route("/update_employee", methods=["GET"])         
def update_employee_info():

    url_params= request.args

    emp_id = int(url_params.get("emp_id"))
    name = url_params.get("name")
    address = url_params.get("address")
    branch = url_params.get("branch")

    return update_employee(emp_id = emp_id, name = name, address = address, branch = branch)

# Delete
# http://localhost:8000/delete_employee?emp_id=99
@app.route("/delete_employee", methods=["GET"])         
def delete_employee_info():

    url_params= request.args

    emp_id = int(url_params.get("emp_id"))
    name = url_params.get("name")
    address = url_params.get("address")
    branch = url_params.get("branch")

    return delete_employee(emp_id = emp_id, name = name, address = address, branch = branch)


###ORDERS###

#make order
@app.route("/make_order/<int:car_id>/<int:customer_id>", methods=["POST"])
def create_order(car_id,customer_id):
    return make_order(car_id=car_id,customer_id=customer_id)

#list all orders
@app.route("/get_orders", methods=["GET"])
def get_orders():
    return findAllOrders()

#cancel order
@app.route("/cancel_order/<int:customer_id>/<int:car_id>", methods=["POST"])
def delete_order(car_id,customer_id):
    return cancel_order_car(car_id=car_id,customer_id=customer_id)



###DIV TESTER###

@app.route("/check_availability/<int:car_id>", methods=["GET"])    
def available(car_id):

    
    return check_availability(car_id=car_id)

@app.route("/check_order/<int:customer_id>/<int:car_id>", methods=["GET"])    
def is_order(customer_id,car_id):

    
    return order_exists(customer_id=customer_id,car_id=car_id)