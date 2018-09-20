__author__ = 'Dreyke Boone'

# TODO this menu option adds a row of data to the database

import sqlite3

def add_row():

    db_file = 'products_db.sqlite'

    game = input("Enter game title: ")
    price = float(input("Enter retail price: "))
    dev = input("Enter game developer: ")
    inv = int(input("Enter amount in inventory: "))
    plat = input("Enter platforms: ")
    rel = input("Enter a date (i.e 09-18-2018): ")

    # connecting to database file
    connect = sqlite3.connect(db_file)
    c = connect.cursor()

    c.execute('INSERT INTO game_products(title, retail_price, developer, inventory, platforms, release_date) VALUES (?, ?, ?, ?, ?, ?)',
              (game, price, dev, inv, plat, rel))

    connect.commit()
    connect.close()

    print("Database has been updated with the following data:"
          "\n", game, "\n", price, "\n", dev, "\n", inv, "\n", plat, "\n", rel)