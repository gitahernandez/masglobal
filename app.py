# app.py
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import logging
import json
from controllers.employees_controller import EmployeesController


app = Flask(__name__)     

@app.route("/api/employes/<employee_id>")
@cross_origin()                
def get_all(employee_id):
    controller = EmployeesController()
    status, result = controller.get_employees(employee_id)
    if status == 200 and result:
        result_json = json.dumps(result.__dict__)
        return result_json
    return result, status

@app.route("/api/employes/")
@cross_origin()                   
def get_by_id():
    controller = EmployeesController()
    status, result = controller.get_employees(None)
    if status == 200 and result:
        result_json = json.dumps([employee.__dict__ for employee in result])
        return result_json
    return result, status

if __name__ == "__main__":        
    app.run()