__author__ = 'Dreyke Boone'

import sqlite3

def search():

    db_file = 'products_db.sqlite' # name of sqlite database file

    # allows user to search for a row based on title
    row_selection = input("Search by game title: ")

    try:
        # connecting to database file
        connect = sqlite3.connect(db_file)
        c = connect.cursor()

        # get row data based on user input
        c.execute("SELECT id, title, retail_price, developer, inventory, platforms, release_date FROM game_products WHERE title=?", (row_selection,))

        rows = c.fetchall()

        if len(rows) == 0:
            print('There is no game title named %s' % row_selection)

        else:
            # display row information to user
            for row in rows:
                print("\nID = ", row[0])
                print("Game Title = ", row[1])
                print("Retail Price = ", row[2])
                print("Developer = ", row[3])
                print("Inventory = ", row[4])
                print("Platforms = ", row[5])
                print("Release Date = ", row[6])

            connect.close()

    except:
        print("An error has occurred. Try again or contact system administrator.")