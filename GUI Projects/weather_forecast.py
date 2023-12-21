import sys
sys.path.append("/mnt/Work/Github/Python-Projects/modules")

import tkinter as tk
import ttkbootstrap as ttk
from weather import Weather

def logic():
    """
    This function is triggered when the user clicks the "Search" button.
    It retrieves weather information based on the city entered by the user.
    Updates the GUI labels with the fetched weather data.
    """
    # Get the city entered by the user
    var = city.get()
    
    # Create a Weather object for the specified city
    weather = Weather(var)
    
    try:
        # Try to fetch temperature, weather description, and wind information
        temperature = weather.temperature()[0]
        weather_1 = weather.weather()[1]
        wind_1 = weather.wind()
    except TypeError:
        # Handle the case where an error occurs (e.g., city not found)
        for i in [temp, weather_info, wind_info]:
            i.set("Some Error occurred.")
        return

    # Update the GUI labels with the fetched weather data
    temp.set(f"Current temperature is {round(temperature, 2)}°C.")
    weather_info.set(f"Step outside and experience the current weather: it's {weather_1} day.")
    wind_info.set(f"Current wind speed is {wind_1[0]}.")

# Create the main application window
window = ttk.Window(themename="darkly")
window.title("Weather Forecast")
window.geometry("540x300")

# Heading
title_label = ttk.Label(text="Weather Forecast", master=window, font=("Silkscreen", 22))
title_label.pack()

# Input area
input_frame = ttk.Frame(master=window)

# Create an Entry widget for the user to input the city
city = tk.StringVar()
input_query = ttk.Entry(master=input_frame, textvariable=city, width=25, font=("Atkinson Hyperlegible", 10))

input_frame.pack(pady=10)
input_query.pack()

# Create a button for the user to trigger the weather search
submit_button = ttk.Button(master=window, text="Search", command=logic)
submit_button.pack(pady=2)

# Create labels to display temperature, weather info, and wind info
font = ("Atkinson Hyperlegible", 12)

temp = tk.StringVar()
temperature_label = ttk.Label(master=window, textvariable=temp, font=font)

weather_info = tk.StringVar()
weather_info_label = ttk.Label(master=window, textvariable=weather_info, font=font)

wind_info = tk.StringVar()
wind_info_label = ttk.Label(master=window, textvariable=wind_info, font=font)

# Pack the labels into the window
temperature_label.pack()
weather_info_label.pack()
wind_info_label.pack()

# Start the Tkinter event loop
window.mainloop()
