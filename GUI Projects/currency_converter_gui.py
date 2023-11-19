import tkinter as tk
import ttkbootstrap as ttk
import sys
sys.path.append("/mnt/Work/Python/Projects/modules")

import currency_converter as cc # type: ignore

def test():
    try: 
        input_var = currFrom.get()
        output_var = currTo.get()
        amount_var = amount.get()
    except tk.TclError as e:
        print(f"Caught Error: {e}\nCheck the entered values")
        return

    final_output.set(cc.Main().convert(input_var, output_var, amount_var))


window = ttk.Window(themename = "darkly")
window.title("Currency Converter")
window.geometry(f"450x200")

title_label = ttk.Label(text = "Currency Converter", master = window, font = ("Silkscreen", 24))
title_label.pack()

input_frame = ttk.Frame(master = window)

input_query = ttk.Label(text = "From: ", master = input_frame, font = ("Anonymous Pro", 14, "bold"))

# variable for input currency
currFrom = ttk.StringVar()
input_entry = ttk.Entry(master = input_frame, textvariable = currFrom, width = "8")

output_query = ttk.Label(text = "To: ", master = input_frame, font = ("Anonymous Pro", 14, "bold"))

# variable for output currency
currTo = ttk.StringVar()
output_entry = ttk.Entry(master = input_frame, textvariable = currTo, width = "8")

# variable for amount
amount = ttk.DoubleVar()
amount_entry = ttk.Entry(master = input_frame, textvariable = amount, width = "8")

input_query.pack(side = "left", padx = 5)
input_entry.pack(side = "left", padx = 5)
output_query.pack(side = "left", padx = 5)
output_entry.pack(side = "left", padx = 5)
amount_entry.pack(side = "left", padx = 5)

input_frame.pack(pady = 10)

convert_button = ttk.Button(master = window, text = "Convert", command = test)
convert_button.pack()

final_output = ttk.StringVar()
final = ttk.Label(master = window, text = "Output", font = ("Atkinson Hyperlegible", 16), textvariable = final_output)
final.pack(pady = 10)

window.mainloop()