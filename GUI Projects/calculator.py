# GUI Calculator - well not an actual calculator as I will be using eval() function. I know it's not recommended but I will include a check for the entries that the user makes

import tkinter as tk
import ttkbootstrap as ttk

def logic():
	queryInput = query.get()
	if queryInput == "": 
		outputString.set("This won't work")
		return
	check = [True if i in "1234567890+-/*%." else False for i in queryInput]
	
	try:
		if False in check:
			outputString.set("Invalid characters were found in your input.")
		else:
			outputString.set(round(eval(queryInput), 4))
	except Exception as e:
		raise SyntaxError(f"E: {str(e)}")

window = ttk.Window(themename = "darkly")
window.title("Calculator")
window.geometry("420x150")

title_label = ttk.Label(master = window, text = "Calculator", font = ("Silkscreen", 20)) 
title_label.pack()

input_frame = ttk.Frame(master = window)

query = ttk.StringVar()

entry = ttk.Entry(master = input_frame, textvariable = query, width = 30)
button = ttk.Button(master = input_frame, text = "Calculate", command = logic)

entry.pack(side = "left", padx = 10)
button.pack(side = "left", padx = 10)
input_frame.pack(pady = 10)

outputString = ttk.DoubleVar()
output = ttk.Label(master = window, text = "Output", font = ("Atkinson Hyperlegible", 16), textvariable = outputString)
output.pack()

window.mainloop()