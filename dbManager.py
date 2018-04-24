# calling sqlite3 traceback is from python library
import sqlite3, traceback
# This will create or open database
dbName = 'items.db'#name of the database

# This is connecting to the database
db = sqlite3.connect(dbName)

# This is the pointer for the data base
cur = db.cursor()



# adding a new item to the database
def addToDb(User, itemName):
    try:
        # calling the create table method
        createItemTable()
        # PLacing the items primary information into the table
        cur.execute('INSERT INTO itemsInventory VALUES(?,?,?)', (itemNumber, User, itemName))

# exception if there is a error accessing sqlite3
    except sqlite3.Error as error:
        print(error)
        traceback.print_exc()

# Creates a table if one doesn't exist in the database
def createItemTable():
    cur.execute('CREATE TABLE IF Not EXISTS itemsInventory (itemNumber INTEGER PRIMARY KEY, User TEXT, itemName TEXT)')

def searchOneItem(itemName):
    itemRecord = cur.execute("Select * from itemsInventory WHERE itemName = ?", (itemName,))
    return itemRecord

def updateItem(itemNumber, updateItem, updateTo):
    cur.execute('UPDATE itemsInventory set {} = ? where itemName = ?'.format(updateItem),(itemNumber, updateTo))

def deleteItem(itemNumber):
    cur.execute('DELETE FROM itemsInventory WHERE itemNumber = ?', (itemNumber))

# This fuction is to fetch all the items in the inventory
def retrieveItems():
    return cur.execute('SELECT * FROM itemsInventory ORDER BY itemName').fetchall()

def exittingApp():
    db.close()
