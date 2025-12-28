"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect('dogs.db')
cursor = conn.cursor()               


# Create a dogs table with autoincrementing ID
def create_dogs_table():
    cursor.execute('''create table if not exists dogs(id integer primary key AUTOINCREMENT,name text not null,breed text,age integer)''')
    conn.commit()

    """TODO"""


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):
    cursor.execute("insert into dogs(name,breed,age)values(?,?,?)",(name,breed,age))
    conn.commit()

    """TODO"""


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():
    cursor.execute('select * from dogs')
    conn.commit()

    # return the rows
<<<<<<< HEAD
    return cursor.fetchall()
=======
    return cursor.fetchall()"""TODO"""
>>>>>>> cd2465fdbb45837fab93ad93be7c01ad03e85e85
