## A simple weather API that connects to the AirNow API for the unites states,
## and returns a JSON objects based on the sate code input.

## Output is the airquality rating, displayed in the relative rating color.

## Some sample codes includes: 90210 , 11225

from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Cal")
root.geometry('430x250')
root.iconbitmap("cal.ico")

# Calls an API, uses the data to create a label, and displays it
def zip_lookup():
	try:
		global frame
		global zipbox
		frame.grid(row=3, column=0, padx=15, pady=15)
		# Request an API using the zipcode as a portion of the HTTPS request
		api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zipbox.get() + "&date=2022-11-08&distance=5&API_KEY=EF493ADC-14F1-4C90-80CA-DFA74FB135D7")
		# Places the API information into an organized JSON file
		api = json.loads(api_request.content)
		# Assigns the appropriate values to their variables
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']
		quality_colour = 'white'
		if category == "Good":
			quality_colour = '#0C0'
		elif category == "Moderate":
			quality_colour = 'FFFF00'
		elif category == "Unhealthy for Sensitive Groups":
			quality_colour = 'ff9900'
		elif category == "Unhealthy":
			quality_colour = 'FF0000'
		elif category == "Very Unhealthy":
			quality_colour = '990066'
		elif category == "Hazardous":
			quality_colour = '660000'

		# Places the data into the frame in the form of a label
		my_label = Label(
			frame, 
			text=city + ", Air Quality: " + str(quality) + ", " + category,
			font=("Helvetica", 15),
			background=quality_colour
		)
		my_label.pack()

	except Exception as error:
		api = "Error..."

# Creates and entry box for zipcode entries
zipbox = Entry(root)
# Performs the lookup function on the code inside the entry box
zip_btn = Button(
	root, 
	text="Lookup Zipcode: ", 
	command=zip_lookup
	)
# Creates a frame into what the data will be show
frame = LabelFrame(
	root, 
	text="Data", 
	padx=10, 
	pady=10, 
	height=100, 
	width=400
	)

# Place Grid items
zipbox.grid(row=0, column=0, pady=20)
zip_btn.grid(row=2, column=0)
frame.grid(
	row=3, 
	column=0, 
	padx=15, 
	pady=15
	)

# Creates and packs default starting label into frame
my_label = Label(
	frame, 
	text="Please select a zipcode for data:",
	font=("Helvetica", 20),
	fg='gray',
	padx=40
	)
my_label.pack()

root.mainloop()