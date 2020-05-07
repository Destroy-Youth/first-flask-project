from flask import Flask, jsonify
from employees import employees


app = Flask(__name__)


@app.route('/test')
def test():
    return 'working!'


@app.route('/employees')
def findEmployees():
    return jsonify({
        "employees": employees
    })


@app.route('/employees/<employeeId>')
def findEmployeeById(employeeId):

    employee_found = unique_employee(employeeId)
    return jsonify({
        "employee": employee_found
    })


def unique_employee(employee_id):

    for employee in employees:
        print(employee['id'])
        if employee['id'] == employee_id:
            return employee

    raise Exception('No employee found with that id')


if __name__ == '__main__':
    app.run(debug=True, port=9000)
