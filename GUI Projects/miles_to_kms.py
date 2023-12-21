import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def logic():
    mileInput = entryInteger.get()
    kmOutput = mileInput * 1.61
    outputString.set(f"{mileInput} miles in kms is {kmOutput} kms")

# Creating a window
window = ttk.Window() # be careful here
window.title("Demo Project")
window.geometry("400x150")

# title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Silkscreen 20")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window) # creating a container to hold the entry field and the button

entryInteger = tk.IntVar() # creating a variable 

entry = ttk.Entry(master = input_frame, textvariable = entryInteger)
button = ttk.Button(master = input_frame, text = "Convert", command = logic)

entry.pack(side = "left", padx=10)
button.pack(side = "left")

input_frame.pack(pady = 10)

# output
outputString = tk.StringVar()

output_label = ttk.Label(
        master = window, 
        text = "Output", 
        font = ("Atkinson Hyperlegible", 16), 
        textvariable = outputString)

output_label.pack(pady = 5)

# run
window.mainloop()
