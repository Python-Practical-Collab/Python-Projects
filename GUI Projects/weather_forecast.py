from os import nice
import sys
sys.path.append("/mnt/Work/Github/Python-Projects/modules")

import tkinter as tk
import ttkbootstrap as ttk
from weather import Weather

def logic():
    var = city.get()
    weather = Weather(var)
    
    
    try:
        temperature = weather.temperature()[0]
        weather = weather.weather()[1]
    except TypeError:
        temp.set("Some Error Occured")
        weather_info.set("Some Error Occured")
        return

    temp.set(f"Current temperature is {round(temperature, 2)}°C.")
    weather_info.set(f"Step outside and experience the current weather: it's a {weather} day.")

window = ttk.Window(themename = "darkly")
window.title("Weather Forecast")
window.geometry("500x500")

# Heading
title_label = ttk.Label(text = "Weather Forecast", master = window)
title_label.pack()

# Input area
input_frame = ttk.Frame(master = window)

city = tk.StringVar()
input_query = ttk.Entry(master = input_frame, textvariable = city)

input_query.pack(pady = 10)
input_frame.pack(pady = 10)

submit_button = ttk.Button(master = window, text = "Search", command = logic)
submit_button.pack()

temp = tk.StringVar()
temperature_label = ttk.Label(master = window, textvariable = temp)

weather_info = tk.StringVar()
weather_info_label = ttk.Label(master = window, textvariable = weather_info) 


temperature_label.pack()
weather_info_label.pack()


window.mainloop()
