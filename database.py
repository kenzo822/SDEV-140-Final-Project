
from collections import Counter
from logging import root
from re import sub
from sre_parse import State
from tkinter import *
import sqlite3


root =Tk()
root.geometry("400x400")


# Database


# Create or connect to a database
conn = sqlite3.connect('Pharmaceutical.db')

# Create a cursor
c = conn.cursor()

#Create table

# table = """ CREATE TABLE pharmaceutical (
#         First_name text,
#         Last_name text, 
#         address text,
#         idnumber integer,
#         socialsecurity integer
#         )""")

# c.execute(table)



# Create a Submit Function For database
def submit():
    # Create or connect to a database
    conn = sqlite3.connect('pharmaceutical.db')
    # Create a cursor
    c = conn.cursor()

   
    # Insert Into Table
    c.execute("INSERT INTO pharmaceutical VALUES (:f_name, :l_name, :address, :idnumber, :socialsecurity)",
            {
                
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'idnumber': idnumber.get(),
                'socialsecurity': socialsecurity.get()
            }
    )



    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()



    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    idnumber.delete(0, END)
    socialsecurity.delete(0, END)

# Create Query Function
def query():
    return



# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
idnumber = Entry(root, width=30)
idnumber.grid(row=3, column=1, padx=20)
socialsecurity = Entry(root, width=30)
socialsecurity.grid(row=4, column=1, padx=20)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
idnumber_label = Label(root, text="Id number")
idnumber_label.grid(row=3, column=0)
socialsecurity_label = Label(root, text="Social Security")
socialsecurity_label.grid(row=4, column=0)

# Creating Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop() 