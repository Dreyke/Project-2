__author__ = 'Dreyke Boone'

# TODO the program deletes a row

import sqlite3

def delete_row():

    db_file = 'products_db.sqlite'

    row_selection = input("Enter a game title to display information: ")

    # connecting to database file
    connect = sqlite3.connect(db_file)
    c = connect.cursor()

    c.execute("SELECT * FROM game_products WHERE title=?", (row_selection,))

    rows = c.fetchall()

    for row in rows:
        print(row)

    step = input("Do you want to delete this game information from the database? (Y/N)")

    if step == 'y':
        warning = input("WARNING!! You are about to delete data from the database! Please confirm you wish to delete this data: Y/N ")
        if warning == 'y':

            c.execute("DELETE FROM game_products WHERE title=?", (row_selection,))
            print("All data related to " + row_selection + " has been deleted.")

            connect.commit()
            connect.close()

        else:
            print("Closing connection to database")

    else:
        print("No data has been deleted.")


