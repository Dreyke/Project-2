__author__ = 'Dreyke Boone'

import sqlite3

# function to update a row in db
def update_row():

    db_file = 'products_db.sqlite' # name of database file

    row_selection = ''

    while row_selection != 'q':

        row_selection = input("Enter a game title to display and update information or press q to quit: ")

        try:
            # connecting to database file
            connect = sqlite3.connect(db_file)
            c = connect.cursor()

            c.execute("SELECT * FROM game_products WHERE title=?", (row_selection,))

            rows = c.fetchall()

            if len(rows) == 0:
                print('There is no game title named %s' % row_selection)
            else:
                for row in rows:
                    print("\nID = ", row[0])
                    print("Game Title = ", row[1])
                    print("Retail Price = ", row[2])
                    print("Developer = ", row[3])
                    print("Inventory = ", row[4])
                    print("Platforms = ", row[5])
                    print("Release Date = ", row[6], "\n")

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
                    connect.commit()
                elif selection == 'retail price':
                    updated_price = input("New retail price: ")
                    c.execute("UPDATE game_products SET retail_price=? WHERE title=?", (updated_price, row_selection,))
                    connect.commit()
                elif selection == 'developer':
                    updated_developer = input("New developer: ")
                    c.execute("UPDATE game_products SET developer=? WHERE title=?", (updated_developer, row_selection,))
                    connect.commit()
                elif selection == 'inventory':
                    updated_inventory = input("Updated inventory: ")
                    c.execute("UPDATE game_products SET inventory=? WHERE title=?", (updated_inventory, row_selection,))
                    connect.commit()
                elif selection == 'platform':
                    updated_platform = input("Updated platforms: ")
                    c.execute("UPDATE game_products SET platforms=? WHERE title=?", (updated_platform, row_selection,))
                    connect.commit()
                elif selection == 'release date':
                    updated_release = input("Updated release date: ")
                    c.execute("UPDATE game_products SET release_date=? WHERE title=?", (updated_release, row_selection,))
                    connect.commit()
                else:
                    print("Error. Please enter a valid entry.")


                exit = input("Do you want add more data? (Y/N)")

                if exit == 'n':
                    connect.close()
                    break

        except:
            print("SQL error occurred. Try again or contact system administrator.")

    print("Database has been updated.")