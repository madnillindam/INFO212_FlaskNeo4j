# from project import app
# from flask import render_template, request, redirect, url_for
# from project.models.my_dao_endpoints import *


# @app.route("/get_cars", methods=["GET"])
# def query_records():
#     return findAllCars()

# # Find car object by ID_number
# @app.route("/get_cars_by_id_number", methods=["POST"])
# def find_car_by_id_number():
#     record = json.loads(request.data)
#     print(record)
#     print(record["car_id"])

# # Save car
# @app.route("/save_car", methods=["POST"])
# def save_car_info():
#     record = json.loads(request.data)
#     print(record)
#     return save_car(record["make"], record["model"], record["car_id"], record["year"], record["location"], record["car_state"])

# # Update car
# @app.route("/update_car", methods=["PUT"])
# def update_car_info():
#     record = json.loads(request.data)
#     print(record)
#     return update_car(record["make"], record["model"], record["car_id"], record["year"], record["location"], record["car_state"])