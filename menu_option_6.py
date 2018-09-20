__author__ = 'Dreyke Boone'

# TODO this menu displays a single row of data based on input value

import sqlite3

def search():

    db_file = 'products_db.sqlite'

    row_selection = input("Enter a game title: ")

    # connecting to database file
    connect = sqlite3.connect(db_file)
    c = connect.cursor()

    c.execute("SELECT id, title, retail_price, developer, inventory, platforms, release_date FROM game_products WHERE title=?", (row_selection,))

    rows = c.fetchall()

    for row in rows:
        print(row)

    connect.close()

search()