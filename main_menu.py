__author__ = 'Dreyke Boone'

import menu_option_1
import menu_option_2
import menu_option_3
import menu_option_4
import menu_option_5
import menu_option_6

print("Pick a menu option or press q to quit")

menu = ''

while menu != 7:

    menu = int(input(""
                     "1. Create a database\n"
                     "2. Add data\n"
                     "3. Update data\n"
                     "4. Delete data\n"
                     "5. Display all data\n"
                     "6. Search for data\n"
                     "7. Exit\n"))

    if menu == 1:
        menu_option_1.create_db()
    elif menu == 2:
        menu_option_2.add_row()
    elif menu == 3:
        menu_option_3.update_row()
    elif menu == 4:
        menu_option_4.delete_row()
    elif menu == 5:
        menu_option_5.display_data()
        break
    elif menu == 6:
        menu_option_6.search()
        break
    elif menu == 7:
        print("Exiting menu.")
        break
    else:
        print("Invalid option. Please select a valid menu option.")