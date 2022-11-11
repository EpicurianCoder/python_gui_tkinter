from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Cal")
root.geometry('300x180')
root.iconbitmap("cal.ico")

# Creates a yes or no pop-up, and prints a label with the answer
def popup_yn():
	response = messagebox.askyesno("This is my popup", "Yes... or NO?")
	if response == 1:
		Label(root, text="you clicked yes").pack()
	else: 
		Label(root, text="you clicked no").pack()
	return

# Creates a customized pop-up warning, prints response
def popup_w():
	response = messagebox.showwarning("Question", "Are you okay?")
	Label(root, text=response).pack()
	return

# Creates three button, each withj a custom command
Button(root, text="Yes/No", command=popup_yn).pack()
Button(root, text="Question", command=popup_w).pack()
Button(root, text="Exit", command=root.quit).pack()

root.mainloop()