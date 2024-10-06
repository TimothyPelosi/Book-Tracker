import os
import sqlite3

# Check to see if the books.db database exists, if not then create it.
def doesDatabaseExist():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_name = 'books.db'
    db_path = os.path.join(current_directory, db_name)

    if os.path.isfile(db_path):
        print(f'Database found: {db_path}')
    else:
        createDatabase()

# Create books.db
def createDatabase():
    db_connect = sqlite3.connect('books.db')
    cursor = db_connect.cursor()
    cursor.execute('''CREATE TABLE books
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT,     
                name TEXT,
                author TEXT
                )''')

def addNewBook():
    print("add new book")

def searchBook():
    print("search books")

def userBookInput(userInput):
    match userInput:
        case 1:
            searchBook()
        case 2:
            addNewBook()
        case _:
            return "Improper input"

def userOptions():
    print("Please select from the following options: ")
    print("1: Search if a book has been read already.")
    print("2: Enter a new book into the database.")
    userInput = int(input("Please enter either 1 or 2: "))
    return userInput

doesDatabaseExist()

db_connect = sqlite3.connect('books.db')
cursor = db_connect.cursor()

userInput = userOptions()
userBookInput(userInput)

