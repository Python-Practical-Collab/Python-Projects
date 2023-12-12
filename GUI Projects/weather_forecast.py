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
        weather_1 = weather.weather()[1]
        wind_1 = weather.wind()
    except TypeError:
        for i in [temp, weather_info, wind_info]:
            i.set("Some Error occured.")
        return

    temp.set(f"Current temperature is {round(temperature, 2)}°C.")
    weather_info.set(f"Step outside and experience the current weather: it's {weather_1} day.")
    wind_info.set(f"Current wind speed is {wind_1[0]}.")

window = ttk.Window(themename = "darkly")
window.title("Weather Forecast")
window.geometry("540x300")

# Heading
title_label = ttk.Label(text = "Weather Forecast", master = window, font = ("Silkscreen", 22))
title_label.pack()

# Input area
input_frame = ttk.Frame(master = window)

city = tk.StringVar()
input_query = ttk.Entry(master = input_frame, textvariable = city, width = 25, font = ("Atkinson Hyperlegible", 10))

input_frame.pack(pady = 10)
input_query.pack()

submit_button = ttk.Button(master = window, text = "Search", command = logic)
submit_button.pack(pady = 2)

font = ("Atkinson Hyperlegible", 12)

temp = tk.StringVar()
temperature_label = ttk.Label(master = window, textvariable = temp, font = font)

weather_info = tk.StringVar()
weather_info_label = ttk.Label(master = window, textvariable = weather_info, font = font) 

wind_info = tk.StringVar()
wind_info_label = ttk.Label(master = window, textvariable = wind_info, font = font)

temperature_label.pack()
weather_info_label.pack()
wind_info_label.pack()

window.mainloop()
