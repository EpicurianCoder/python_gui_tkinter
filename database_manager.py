## Simple Database Management GUI using SQLite 

## Create, delete, view and edit entries into a SQLite DB

from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Cal")
root.geometry('650x500')
root.iconbitmap("cal.ico")

# creates/connects to database
connection = sqlite3.connect('database_created_sqlite3.db')

# Create cursor
cursor = connection.cursor()

# ## Intial creation of database structure (run once)
# cursor.execute("""
# 	CREATE TABLE my_database (
# 		first_name text,
# 		last_name text,
# 		city text,
# 		zipcode int
# 	)
# 	""")

# Using the OID argument as ref, inputs various entrybox data to DB
def save(oid):
	connection = sqlite3.connect('database_created_sqlite3.db')
	cursor = connection.cursor()
	cursor.execute("""
		UPDATE my_database SET 
			first_name = :first,
			last_name = :last_name,
			city = :city,
			zipcode = :zipcode
			WHERE oid = :oid""",
			{
				'first': first_name_editor.get(),
				'last_name' : last_name_editor.get(),
				'city' : city_editor.get(),
				'zipcode' : zipcode.get(),
				'oid': oid
			})
	# Commit and close our connection after each each
	connection.commit()
	connection.close()
	# Show that save has been successful
	note = messagebox.showwarning("Saved", "Saved to Database!")
	# Removes the pre-populated editor we created for the OID
	editor.destroy()
	return

# Creates an update function for the SQLite3 database
def update(oid):
	global editor
	# Creates an entirely new window
	editor = Tk()
	editor.title("Update")
	editor.geometry('650x220')
	connection = sqlite3.connect('database_created_sqlite3.db')
	cursor = connection.cursor()
	# Selects all data relevant to OID
	cursor.execute("SELECT * FROM my_database WHERE oid=" + oid)
	records = cursor.fetchall()

	# Create global text box variables
	global first_name_editor
	global last_name_editor
	global city_editor
	global zipcode_editor

	# Creates and places entry boxes
	first_name_editor = Entry(editor, width=50)
	first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
	last_name_editor = Entry(editor, width=50)
	last_name_editor.grid(row=1, column=1, padx=20)
	city_editor = Entry(editor, width=50)
	city_editor.grid(row=2, column=1, padx=20)
	zipcode_editor = Entry(editor, width=50)
	zipcode_editor.grid(row=3, column=1, padx=20)

	# Creates and places Labels
	f_name_label = Label(editor, text="First Name")
	f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
	last_name_label = Label(editor, text="Last Name")
	last_name_label.grid(row=1, column=0, padx=20)
	city_label = Label(editor, text="City")
	city_label.grid(row=2, column=0, padx=20)
	zipcode_label = Label(editor, text="zipcode")
	zipcode_label.grid(row=3, column=0, padx=20)

	# Inserts the OID data into the entry boxes
	for record in records:
		first_name_editor.insert(0, record[0])
		last_name_editor.insert(0, record[1])
		city_editor.insert(0, record[2])
		zipcode_editor.insert(0, record[3])

	# Executes saves function using the oid as the argument
	save_btn = Button(
		editor, 
		text="Edit Record", 
		command=lambda: save(oid))
	save_btn.grid(
	row=4, 
	column=0,
	columnspan=2,
	pady=10,
	padx=10,
	ipadx=137)

	connection.commit()
	connection.close()

	return

# Open a connects and deletes all data relation to given oid
def delete():
	connection = sqlite3.connect('database_created_sqlite3.db')
	cursor = connection.cursor()
	# delete a record
	cursor.execute("DELETE FROM my_database WHERE oid="+ select_box.get())
	connection.commit()
	connection.close()
	select_box.delete(0, END)
	query()

# return all the items from the database, formate and displays them
def query():
	print_records = ''
	connection = sqlite3.connect('database_created_sqlite3.db')
	cursor = connection.cursor()
	# Using oid as key, selects all the columns and rows
	cursor.execute("SELECT *, oid FROM my_database")
	records = cursor.fetchall()
	for record in records:
		print_records += "Name: " + str(record[0]) + "\t" + "OID: " + str(record[4]) + "\n"
	if len(print_records) > 0:
		qlabel = Label(root, text=print_records)
		qlabel.grid(row=8, column=0, columnspan=2)
	else: 
		qlabel = Label(root, text="Database Empty")
		qlabel.grid(row=8, column=0, columnspan=2)
	connection.commit()
	connection.close()

# Using the entry box input, creates a new entry in the database
def submit():
	data = [
		(first_name.get()),
		(last_name.get()),
		(city.get()),
		(zipcode.get())
	]
	connection = sqlite3.connect('database_created_sqlite3.db')
	cursor = connection.cursor()
	if (len(first_name.get()) > 0) & (len(last_name.get()) > 0) & (len(city.get()) > 0) & (len(zipcode.get()) > 0):
		cursor.execute("""
			INSERT INTO my_database 
			VALUES (?,?,?,?)"""
			, data)
	# Ensures the entryboxes are full, and data remains uncorrupted.
	else:
		messagebox.showwarning(title="Error", message="All fields must be completed")
	# Clears textboxes
	first_name.delete(0, END)
	last_name.delete(0, END)
	city.delete(0, END)
	zipcode.delete(0, END)
	# Closes connection
	connection.commit()
	connection.close()
	query()

# Create text boxes
first_name = Entry(root, width=50)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
last_name = Entry(root, width=50)
last_name.grid(row=1, column=1, padx=20)
city = Entry(root, width=50)
city.grid(row=2, column=1, padx=20)
zipcode = Entry(root, width=50)
zipcode.grid(row=3, column=1, padx=20)

# Creates Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0, padx=20)
city_label = Label(root, text="City")
city_label.grid(row=2, column=0, padx=20)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=3, column=0, padx=20)
select_label = Label(root, text="Select by OID: ")
select_label.grid(row=9, column=0, padx=20, pady=(10, 0))
select_box = Entry(root, width=50)
select_box.grid(row=9, column=1, padx=20, pady=(10, 0))

# Creates and places buttons
submit_btn = Button(
	root, 
	text="Submit", 
	command=submit
	)
submit_btn.grid(
	row=4, 
	column=0,
	columnspan=2,
	pady=10,
	padx=10,
	ipadx=137)
query_btn = Button(
	root, 
	text="Show Records", 
	command=query
	)
query_btn.grid(
	row=7, 
	column=0,
	columnspan=2, 
	pady=10,
	padx=10,
	ipadx=115
	)
delete_btn = Button(
	root, 
	text="Delete", 
	command=delete
	)
delete_btn.grid(
	row=13, 
	column=0,
	columnspan=2, 
	pady=10,
	padx=10,
	ipadx=115
	)
update_btn = Button(
	root, 
	text="Update", 
	command=lambda: update(str(select_box.get()))
	)
update_btn.grid(
	row=14, 
	column=0,
	columnspan=2, 
	pady=10,
	padx=10,
	ipadx=115
	)

# commit changes
connection.commit()
# close db connection
connection.close()

root.mainloop()
