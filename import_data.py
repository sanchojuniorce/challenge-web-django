import csv
from dotenv import dotenv_values
from mysql import connector

config = dotenv_values(".env")

# Connect to server
cnx = connector.connect(
    host=config['HOST'],
    port=config['PORT'],
    user=config['USER'],
    password=config['PASSWORD'],
    database=config['DATABASE'])

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * FROM challenge_open_food.products;")

# Fetch one result
row = cur.fetchone()
print(row)

# Close connection
cnx.close()