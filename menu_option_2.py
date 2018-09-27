__author__ = 'Dreyke Boone'

import sqlite3

def get_data():

    global game, price, dev, inv, plat, rel

    # lets the user set data for each column
    game = input("Enter game title: ")
    price = float(input("Enter retail price: "))
    dev = input("Enter game developer: ")
    inv = int(input("Enter amount in inventory: "))
    plat = input("Enter platforms: ")
    rel = input("Enter a date (i.e YYYY-MM-DD): ")

def add_row():

    connect = None

    db_file = 'products_db.sqlite'  # name of sqlite database file

    try:
        # connecting to database file
        connect = sqlite3.connect(db_file)
        c = connect.cursor()

        # adds player defined row into database
        c.execute('INSERT INTO game_products(title, retail_price, developer, inventory, platforms, release_date) VALUES (?, ?, ?, ?, ?, ?)',
                  (game, price, dev, inv, plat, rel))

    except sqlite3.Error as e:
        print("Error %s when inserting data into table. Please try again" % e)

    finally:
        connect.commit()
        connect.close()

    print("Database has been updated with the following data:"
          "\n", game, "\n", price, "\n", dev, "\n", inv, "\n", plat, "\n", rel)

def main():

    try:
        get_data()
    except (ValueError, NameError):
        print("Error. Please type the correct characters.")
        get_data()
    finally:
        add_row()
