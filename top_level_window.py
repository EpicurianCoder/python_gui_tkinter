# A basic program dispaying an image inside its own floating window
# when button is pressed

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Cal")
root.geometry('300x300')
root.iconbitmap("cal.ico")

# Brings up a messagebox and if positive, performs open_()
def click():
	answer = messagebox.askokcancel("Here's an image", "See the image?")
	if answer:
		open_()
	else:
		root.quit()
	return

# Create a new window with Toplevel() function and displays image
def open_():
	global my_img
	top = Toplevel()
	top.title("My inner window")
	label_1 = Label(top, text="Inner Text").pack()
	my_img = ImageTk.PhotoImage(Image.open("images/me.png"))
	my_label = Label(top, image=my_img).pack()

# Button for opening window/image
btn = Button(root, text="Open inner window", command=click).pack()

root.mainloop()