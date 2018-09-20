__author__ = 'Dreyke Boone'

# TODO the menu program updates a row

import sqlite3

def update_row():

    db_file = 'products_db.sqlite'

    update = input("Do you want to update data? (Y/N)")

    while update != 'n':

        # connecting to database file
        connect = sqlite3.connect(db_file)
        c = connect.cursor()

        rows = c.fetchall()

        for row in rows:
            print(row)

        row_selection = input("Enter a game title to display and update information: ")

        selection = input("\nWhat info would you like to update? (Enter one of the following: "
                          "\ntitle"
                          "\nretail price"
                          "\ndeveloper"
                          "\ninventory"
                          "\nplatform"
                          "\nrelease date"
                          "\n")

        if selection == 'title':
            updated_title = input("New game title: ")
            c.execute("UPDATE game_products SET title=? WHERE title=?",(updated_title, row_selection,))
        elif selection == 'retail price':
            updated_price = input("New retail price: ")
            c.execute("UPDATE game_products SET retail_price=? WHERE title=?", (updated_price, row_selection,))
        elif selection == 'developer':
            updated_developer = input("New developer: ")
            c.execute("UPDATE game_products SET developer=? WHERE title=?", (updated_developer, row_selection,))
        elif selection == 'inventory':
            updated_inventory = input("Updated inventory: ")
            c.execute("UPDATE game_products SET inventory=? WHERE title=?", (updated_inventory, row_selection,))
        elif selection == 'platform':
            updated_platform = input("Updated platforms: ")
            c.execute("UPDATE game_products SET platforms=? WHERE title=?", (updated_platform, row_selection,))
        elif selection == 'release date':
            updated_release = input("Updated release date: ")
            c.execute("UPDATE game_products SET release_date=? WHERE title=?", (updated_release, row_selection,))
        else:
            print("Error. Please enter a valid entry.")


        exit = input("Do you want add more data? (Y/N)")

        if exit == 'n':
            connect.commit()
            connect.close()
            break

update_row()