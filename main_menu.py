__author__ = 'Dreyke Boone'

import menu_option_1
import menu_option_2
import menu_option_3
import menu_option_4
import menu_option_5
import menu_option_6

# TODO write menu, call the the other 6 menu options from here
# TODO database should have an ID key and 6 additional product data columns
# TODO Use various data types and constraints such as Not Null, default values, etc

print("Pick a menu option")
menu = int(input(""
                 "1. Create a database\n"
                 "2. Add data\n"
                 "3. Update data\n"
                 "4. Delete data\n"
                 "5. Display all data\n"
                 "6. Search for data\n"))

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
elif menu == 6:
    pass
else:
    pass