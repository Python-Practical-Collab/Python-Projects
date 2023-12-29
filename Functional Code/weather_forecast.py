# weather app
import os
import requests

class Main:

    def __init__(self, location):
        self.location = location
        self.api_key = "cz1FGOOITWK2RE8rsOwKUosR26OS9PH3"
        self.url = f"https://api.tomorrow.io/v4/weather/realtime?location={self.location}&apikey={self.api_key}"
        self.headers = {"accept": "application/json"}

    def make_request(self):
        os.system("clear")
        try:
            response = requests.get(self.url, headers=self.headers).json()
        except Exception as e:
            print(f"Error {e} occured.")
        
        location_data = response.get("location", {})
        weather_data = response.get("data", {})

        # Location Information
        print(f"Weather Forecast for {location_data['type']}: {location_data['name']}")
        print(f"Longitude: {round(location_data['lon'], 4)}, Latitude: {round(location_data['lat'], 4)}")

        # Weather Data
        print("----------------------")
        print(f"Temperatue: {weather_data['temperature']}°C")
        print(f"But, it may feel like {weather_data['temperatureApparent']}°C")
        print(f"Humidity: {weather_data['humidity']}%")

a = Main("Ludhiana").make_request()