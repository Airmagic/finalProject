 # sys is to exit the quit_program
# user_interface is the a file for graphics
 # log controller is a a file for logging
# dbManager is a py file that does all dbcalls
import sys, ui, log_controller, dbManager

# creating variables that are easier to type
logCon = log_controller

# main program
def main():
    dbManager.createItemTable()
    # calling the menu for user and calling the method
    menu_controller(ui.top_menu())

def menu_controller(menu_selection):

    # using a dictionary to control the selection from the user
    selection_dict = {
        '1': searchForItem,
        '2': getAllFromInventory,
        '3': addItem,
        '4': changeItem,
        '5': deleteItem,
        'q': quit_program,
        'Q': quit_program,
    }

    # getting the user selection from user interface and calling related function
    call_function = selection_dict.get(menu_selection)

    # This checks to see if the selection is in the dictionary
    if menu_selection not in selection_dict:
        ui.message('Invalid Selection, Try Again')
        logCon.log_info_message('Tried to enter invalid selection.')
        main()

    # calling the method selected from menu if it valid
    else:
        call_function()

def addItem():
    user = input("Who is the user? ")
    user = formatingInput(user)
    name = input("Name of the item")
    name = formationInput(name)


    main()

def searchForItem():
    searchFor = input('What Item are you looking for? ')
    searchFor = formatingInput(searchFor)
    result = dbManager.searchOneItem(searchFor)
    for row in result:
        print(row)
    main()

def getAllFromInventory():
    dbManager.retrieveItems()
    main()

def addItem():
    main()

def changeItem():
    main()

def deleteItem():
    main()

def formatingInput(itemName):
    return itemName.lower().title()


def quit_program():
    dbManager.exittingApp()
    logCon.log_info_message('Closed the application.')
    sys.exit('Closing \n')


if __name__ == '__main__':
    main()
