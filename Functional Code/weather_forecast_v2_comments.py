import os
import pytz
import requests
from datetime import datetime

class WeatherForecast:

    def __init__(self, location):
        # Initialize the WeatherForecast object with the provided location
        self.location = location
        self.api_key = "00cd4be2b420a9aac2dceca8849fac6f"
        self.geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.location}&limit=1&appid={self.api_key}"

    def make_request(self):
        # Clear the console screen
        os.system("clear")

        # Set the local time zone
        self.local_tz = pytz.timezone('Asia/Kolkata')

        try:
            # Make a request to the OpenWeatherMap Geo API to get coordinates
            response = requests.get(self.geo_url).json()
        except Exception as e:
            print(f"Error: {e} occurred.")

        # Extract location coordinates from the response
        co_ords = [(location["lat"], location["lon"], location["state"], location["country"]) for location in response]
        new_co_ords = [j for i in co_ords for j in i]

        data = ["Latitude", "Longitude", "State", "Country"]
        print(f"Weather Forecast for {self.location}:")
        print("--------------------------")

        # Display location information
        try: 
            for i in range(4):
                print(f"{data[i]} : {new_co_ords[i]}")
            print("--------------------------")
        except Exception as e:
            print("Looks like there are some conflicts with that location. Please be more specific!")
            exit()

        # Set latitude and longitude for weather request
        self.latitude = new_co_ords[0]
        self.longitude = new_co_ords[1]

        # Proceed to get weather information
        self.weather()

    def weather(self):
        # Construct the weather API URL
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}"

        try:
            # Make a request to the OpenWeatherMap Weather API to get current weather
            response = requests.get(weather_url).json()
        except Exception as e:
            print(f"Error: {e} occurred.")

        # Extract relevant weather information from the response
        temps = response.get("main", {})
        sun = response.get("sys", {})
        weather = response.get("weather", {})[0]
        wind = response.get("wind", {})

        # Convert UTC timestamps to local time
        sunrise_utc = datetime.utcfromtimestamp(sun["sunrise"])
        sunset_utc = datetime.utcfromtimestamp(sun["sunset"])

        # Display temperature information
        print(f"Today's Temperature is: {round(temps['temp'] - 273.15, 2)}°C. But, it may feel like {round(temps['feels_like'] - 273.15, 2)}°C")
        print(f"Maximum Temperature for today: {round(temps['temp_max'] - 273.15, 2)}°C")

        # Display weather conditions
        print(f"The current weather conditions suggest {weather['main']} and {weather['description']}, but please note that the weather can change, so it's a good idea to check for updates throughout the day.")

        # Display pressure and humidity
        print(f"Pressure: {round(temps['pressure'] * 0.029529983071445, 4)} psi")
        print(f"Humidity: {temps['humidity']}%")

        print("--------------------------")

        # Display wind information
        print(f"The current wind speed is {wind['speed']} m/s, coming from the direction of {wind['deg']} degrees.")

        print("--------------------------")

        # Display sunrise and sunset times
        print(f"Sun is expected to rise today at {sunrise_utc.replace(tzinfo=pytz.utc).astimezone(self.local_tz)}")
        print(f"Sun is expected to set today at {sunset_utc.replace(tzinfo=pytz.utc).astimezone(self.local_tz)}")

# Create an instance of WeatherForecast and make the request
weather_forecast = WeatherForecast(input("Enter name of the area: "))
weather_forecast.make_request()
