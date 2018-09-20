__author__ = 'Dreyke Boone'

import sqlite3

def create_db():

    db_file = 'products_db.sqlite' # name of sqlite database file
    table_name = 'game_products' # name of table to be created
    id_column = 'id' # name of the PRIMARY KEY column
    title_column = 'title' # game title column
    price_column = 'retail_price' # retail price of game
    developer_column = 'developer' # developer of game
    inventory_column = 'inventory' # amount in inventory
    platforms_column = 'platforms' # which platforms the game is available for
    release_date_column = 'release_date' # game release date

    # connecting to database file
    connect = sqlite3.connect(db_file)
    c = connect.cursor()

    # creating game products table with 7 columns and setting the first column as the
    c.execute('''CREATE TABLE IF NOT EXISTS {tn} 
                ({cn1} INTEGER PRIMARY KEY,
                {cn2} VARCHAR(25) NOT NULL,
                {cn3} DOUBLE NOT NULL,
                {cn4} VARCHAR(25) NOT NULL,
                {cn5} INT,
                {cn6} VARCHAR(25),
                {cn7} REAL)'''\
              .format(tn=table_name, cn1=id_column, cn2=title_column, cn3=price_column, cn4=developer_column,
                      cn5=inventory_column, cn6=platforms_column, cn7=release_date_column))

    connect.commit()
    connect.close()

    # displays list of columns that have been created
    print("Game Products database has been created. The following columns have been added:\n"
          "id\n"
          "Title\n"
          "Price\n"
          "Developer\n"
          "Inventory\n"
          "Platforms\n"
          "Release Date")
