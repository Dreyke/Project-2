__author__ = 'Dreyke Boone'

import sqlite3

def display_data():

    db_file = 'products_db.sqlite' # name of sqlite database file

    # display all rows in database
    print("Here is all the data from the database\n")

    try:
        connect = sqlite3.connect(db_file)
        c = connect.cursor()

        c.execute("SELECT id, title, retail_price, developer, inventory, platforms, release_date FROM game_products")

        for row in c:
            print("\nID = ", row[0])
            print("Game Title = ", row[1])
            print("Retail Price = ", row[2])
            print("Developer = ", row[3])
            print("Inventory = ", row[4])
            print("Platforms = ", row[5])
            print("Release Date = ", row[6])

        connect.close()

    except:
        print("An error has occurred. Please try again.")
