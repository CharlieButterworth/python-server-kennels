import sqlite3
import json
from models import Employee


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.name,
            e.address,
            e.id,
            e.location_id
        FROM employee e 
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['address'],
                                row['location_id'])

            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.name,
            e.address,
            e.id,
            e.location_id
        FROM employee e 
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

    return json.dumps(employee.__dict__)

# def create_employee(employee):
#     # Get the id value of the last employee in the list
#     max_id = EMPLOYEES[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the employee dictionary
#     employee["id"] = new_id

#     # Add the employee dictionary to the list
#     EMPLOYEES.append(employee)

#     # Return the dictionary with `id` property added
#     return employee


# def delete_employee(id):
#     # Initial -1 value for employee index, in case one isn't found
#     employee_index = -1

#     # Iterate the EMPLOYEE list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             # Found the employee. Store the current index.
#             employee_index = index

#     # If the employee was found, use pop(int) to remove it from list
#     if employee_index >= 0:
#         EMPLOYEES.pop(employee_index)


# def update_employee(id, new_employee):
#     # Iterate the EMPLOYEES list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, employee in enumerate(EMPLOYEES):
#         if customer["id"] == id:
#             # Found the customer. Update the value.
#             EMPLOYEES[index] = new_employee
#             break
