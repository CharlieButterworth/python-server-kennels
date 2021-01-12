EMPLOYEES = [
    {
        "name": "Jeremy Bakker",
        "animalId": 2,
        "id": 1,
        "locationId": 2
    },
    {
        "name": "John Smith",
        "animalId": 2,
        "id": 2,
        "locationId": 2
    },
    {
        "name": "Jacob Dunn",
        "animalId": 2,
        "id": 3,
        "locationId": 2
    },
    {
        "name": "Casey Black",
        "animalId": 2,
        "id": 4,
        "locationId": 2
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
