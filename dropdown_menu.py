## Very Simple dropdown GUI fror selecting size

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Select Size")
root.geometry('500x300')
root.iconbitmap("cal.ico")

# Outputs selected option from dropdown to label
def show():
	my_label = Label(root, text=chosen.get()).pack()

# List for dropdown options
options = [
	"Choose Size",
	"Small",
	"Medium",
	"Large"
]

# Tkinter variable variable used for dropdown menu
chosen = StringVar()
chosen.set(options[0])

# Creates our dropdown menu using the tkinter variable and the list
drop = OptionMenu(root, chosen, *options)
drop.pack()
# Catpures and returns the selected item
my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()
