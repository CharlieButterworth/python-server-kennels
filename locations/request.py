import sqlite3
import json
from models import Location


def get_all_locations():

    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.name,
            l.address,
            l.id
        FROM location l
        """)

        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)


# def create_location(location):
#     # Get the id value of the last location in the list
#     max_id = LOCATIONS[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the location dictionary
#     location["id"] = new_id

#     # Add the location dictionary to the list
#     LOCATIONS.append(location)

#     # Return the dictionary with `id` property added
#     return location


# def delete_location(id):
#     # Initial -1 value for location index, in case one isn't found
#     location_index = -1

#     # Iterate the LOCATION list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             # Found the employee. Store the current index.
#             location_index = index

#     # If the location was found, use pop(int) to remove it from list
#     if location_index >= 0:
#         LOCATIONS.pop(location_index)


# def update_location(id, new_location):
#     # Iterate the LOCATIONS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             # Found the location. Update the value.
#             LOCATIONS[index] = new_location
#             break
