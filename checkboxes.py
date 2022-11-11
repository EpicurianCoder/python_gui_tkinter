## Rudimentary checkbox with basic output frame

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple checkbox")
root.geometry('500x300')
root.iconbitmap("cal.ico")

# Creates a frame and populates it with a label using the tkinter variable
def update():
	frame = LabelFrame(
	root, 
	text="This is a frame", 
	padx=100, 
	pady=10
	)
	frame.grid(row=1, column=0, padx=15)
	my_label = Label(frame, text=check_var.get()).pack()

# tkinter variable for the checkobox
check_var = StringVar()
# Checkbox that outputs state when toggled
checkbox = Checkbutton(
	root, 
	text="Are you a hacker?", 
	variable=check_var, 
	command=update,
	onvalue="Hacker",
	offvalue="Innocent Bystander"
	)

# deselects the checkbox by default.
checkbox.deselect()
checkbox.grid(row=0, column=0, sticky=W)

root.mainloop()
