# Getting from the log controoler .py
# import log_controller
# Making it easier to write
# logCon = log_controller

# Program for the user interface
def top_menu():

    message('''
        1) Search For One Item
        2) Search All Items
        3) Add Item
        4) Change Item
        5) Delete Item
        q) Exit
    ''')

    menu_selection = input('Select an option to continue.\n')
    return menu_selection


def message(msg):
    print(msg + '\n')
