# Weather Forecast
import os
import pytz
import requests
from datetime import datetime

class Main:

    def __init__(self, location):
        self.location = location
        self.api_key = "00cd4be2b420a9aac2dceca8849fac6f"
        self.geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.location}&limit=1&appid={self.api_key}"
    
    def make_request(self): 
        os.system("clear")
        self.local_tz = pytz.timezone('Asia/Kolkata')

        try:
            response = requests.get(self.geo_url).json()
            # print(response)
        except Exception as e:
            print(f"{e} occured.")

        co_ords = [(location["lat"], location["lon"], location["state"], location["country"]) for location in response]
        new_co_ords = [j for i in co_ords for j in i]

        data = ["Latitude", "Longitude", "State", "Contry"]
        print(f"Weather Forecast for {self.location}:")
        print("--------------------------")

        for i in range(4):
            print(f"{data[i]} : {new_co_ords[i]}")
        print("--------------------------")
        
        self.latitude = new_co_ords[0]
        self.longitude = new_co_ords[1]

        self.weather()

    def weather(self):
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}"

        try:
            response = requests.get(weather_url).json()
        except Exception as e:
            print(f"{e} occured")

        temps = response.get("main", {})
        sun = response.get("sys", {})
        weather = response.get("weather", {})[0]
        wind = response.get("wind", {})

        sunrise_utc = datetime.utcfromtimestamp(sun["sunrise"])
        sunset_utc = datetime.utcfromtimestamp(sun["sunset"])

        print(f"Today's Temperature is: {round(temps['temp'] - 273, 4)}°C. But, it may feel like {round(temps['feels_like'] - 273, 4)}°C")
        print(f"Maximum Temperature for today: {round(temps['temp_max'] - 273, 4)}°C")
        print(f"The current weather conditions suggest {weather['main']} and {weather['description']}, but please note that the weather can change, so it's a good idea to check for updates throughout the day.")
        print(f"Pressure: {round(temps['pressure'] * 0.029, 4)} psi")
        print(f"Humidity: {temps['humidity']}%")

        print("--------------------------") 
        print(f"The current wind speed is {wind['speed']} m/s, coming from the direction of {wind['deg']} degrees.")

        # Further work required here
        print("--------------------------") 
        print(f"Sun is expected to rise today at {sunrise_utc.replace(tzinfo=pytz.utc).astimezone(self.local_tz)}")
        print(f"Sun is expected to set today at {sunset_utc.replace(tzinfo=pytz.utc).astimezone(self.local_tz)}")


Main("Ludhiana").make_request()