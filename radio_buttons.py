## A simple list in the form of radio buttons, built from a list, 
## and with a capture button that reads the state of the radio 
## buttons and keeps track of the count of each radio item.

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button Order Counter")
root.geometry('300x300')

# Creates a list of possbile items to order
DRINKS = [
	("Coke","Coke"),
	("Fanta","Fanta"),
	("Sprite","Sprite"),
	("Tab","Tab")
]

# A dictionary for keeping track of radio button requests
counters = {
	"Coke":0,
	"Fanta":0,
	"Sprite":0,
	"Tab":0
}

# Tkinter variable for the radio buttons
drink = StringVar()
# Set the intial selection to coke by default
drink.set("Coke")

# Displays name, Increments dictionary counter for drinks clicked
def click(value):
	global counters
	counters[drink.get()] += 1
	my_label = Label(
		root, 
		text=drink.get() + ": Total= " + str(counters[drink.get()]), 
		font=("Helvetiva", 20)
		)
	my_label.pack()

# Creates a button for each item in the DRINK list
for text, contents in DRINKS:
	Radiobutton(
		root, 
		text=text, 
		variable=drink, 
		value=contents
	).pack()

# Captures the current state of the radio buttons and performs click()
myButton = Button(
	root, 
	text="Click Me to Order", 
	command=lambda: click(drink.get())
)
myButton.pack()

root.mainloop()