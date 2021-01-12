CUSTOMERS = [
    {
        "email": "cb@gmail.com",
        "password": "cb",
        "name": "chuck Butters",
        "id": 1
    },
    {
        "email": "t@gmail.com",
        "password": "cam",
        "name": "Tyler",
        "id": 2
    },
    {
        "email": "cv@df",
        "password": "dfdf",
        "name": "Mr. Sir",
        "id": 3
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
