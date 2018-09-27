__author__ = 'Dreyke Boone'

import sqlite3

def delete_row():

    connect = None

    db_file = 'products_db.sqlite'  # name of sqlite database file

    # get title from user to display related row
    row_selection = input("Enter a game title to display information: ")

    try:
        # connecting to database file
        connect = sqlite3.connect(db_file)
        c = connect.cursor()

        # get title from database
        c.execute("SELECT * FROM game_products WHERE title=?", (row_selection,))

        # get entire row related to the title the user entered
        rows = c.fetchall()

        # checks if title/row exists
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
                print("Release Date = ", row[6], "\n")

            # Check if this is the information the user wants to delete
            step = input("Do you want to delete this game information from the database? (Y/N)")

            # if user selects y, than a warning is displayed and they need to confirm they want to delete
            if step == 'y':
                warning = input(
                    "WARNING!! You are about to delete data from the database! This data cannot be restored. Please confirm you wish to delete this data: Y/N ")
                if warning == 'y':

                    c.execute("DELETE FROM game_products WHERE title=?", (row_selection,))
                    print("All data related to " + row_selection + " has been deleted.")

                else:
                    print("Closing connection to database")
            else:
                print("No data has been deleted.")

    except sqlite3.Error as e:
        print("Error %s when deleting data from table. Please try again" % e)

    finally:
        connect.commit()
        connect.close()