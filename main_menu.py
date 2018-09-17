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
                 "6. Search for data\n"
                 "7. Exit\n\n"))

if menu == 1:
    menu_option_1.create_db()
elif menu == 2:
    pass
elif menu == 3:
    pass
elif menu == 4:
    pass
elif menu == 5:
    pass
elif menu == 6:
    pass
else:
    pass