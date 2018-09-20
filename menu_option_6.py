__author__ = 'Dreyke Boone'

# TODO this menu displays a single row of data based on input value
# TODO see if there's a better way to search the database. If not, this is efficient

import sqlite3

def search():

    db_file = 'products_db.sqlite' # name of sqlite database file

    # allows user to search for a row based on title
    row_selection = input("Enter a game title: ")

    # connecting to database file
    connect = sqlite3.connect(db_file)
    c = connect.cursor()

    # get row data based on user input
    c.execute("SELECT id, title, retail_price, developer, inventory, platforms, release_date FROM game_products WHERE title=?", (row_selection,))

    rows = c.fetchall()

    for row in rows:
        print(row)

    connect.close()