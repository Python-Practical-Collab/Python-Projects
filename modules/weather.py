import requests
import logging
from datetime import datetime

class Weather:
    """
    A class to fetch weather information from the OpenWeatherMap API for a specific city.

    Parameters:
        city (str): The name of the city for which weather information is to be fetched.
        api (str, optional): The API key for accessing the OpenWeatherMap API. Defaults to a sample key.

    Attributes:
        apikey (str): The API key for accessing the OpenWeatherMap API.
        city (str): The name of the city for which weather information is fetched.
        city_url (str): The URL for the OpenWeatherMap API endpoint for the specified city.
    """

    def __init__(self, city: str, api: str = "00cd4be2b420a9aac2dceca8849fac6f") -> None:
        """
        Initializes a Weather instance.

        Parameters:
            city (str): The name of the city for which weather information is to be fetched.
            api (str, optional): The API key for accessing the OpenWeatherMap API. Defaults to a sample key.
        """
        self.apikey = api
        self.city = city.capitalize()
        self.city_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apikey}"

        logging.basicConfig(level=logging.INFO)

    def make_request(self):
        """
        Makes a request to the OpenWeatherMap API and retrieves the weather information.

        Returns:
            dict or None: A dictionary containing weather information if successful, None otherwise.
        """
        try:
            response = requests.get(self.city_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error making requests: {e}")
            return None
        except ValueError as e:
            logging.error(f"Error parsing JSON: {e}")
            return None

    def coordinates(self):
        """
        Retrieves the coordinates (longitude, latitude) of the city.

        Returns:
            tuple or None: A tuple containing longitude and latitude if successful, None otherwise.
        """
        result = self.make_request()
        if result:
            loc_query = result.get("coord")
            if loc_query:
                return loc_query["lon"], loc_query["lat"]
            else:
                logging.error("Error getting coordinates.")
        else:
            return None

    def temperature(self):
        """
        Retrieves the temperature (Current, Feels, Min, Max, Humidity) of the city.

        Returns:
            dict or None: A dictionary containing all of the above information in the same order.
        """
        result = self.make_request()
        if result:
            temperature_query = result.get("main")
            if temperature_query:
                return {
                    "Current": temperature_query["temp"] - 273,
                    "Feels": temperature_query["feels_like"] - 273,
                    "Min": temperature_query["temp_min"] - 273,
                    "Max": temperature_query["temp_max"] - 273,
                    "Humidity": temperature_query["humidity"]
                }
            else:
                logging.error("Error getting temperature.")
        else:
            return None

    def wind(self):
        """
        Retrieves the wind (speed, deg) information of the city.

        Returns:
            tuple or None: A tuple containing speed of the wind and the degree from where it's coming.
        """
        result = self.make_request()
        if result:
            wind_query = result.get("wind")
            if wind_query:
                return wind_query["speed"], wind_query["deg"]
            else:
                logging.error("Error getting wind information.")
        else:
            return None

    def weather(self):
        """
        Retrieves current weather (main, description) information of the city.

        Returns:
            tuple or None: A tuple containing information about the current weather information of the city.
        """
        result = self.make_request()
        if result:
            weather_query = result.get("weather")[0]
            if weather_query:
                return weather_query["main"], weather_query["description"]
            else:
                logging.error("Error getting weather information.")
        else:
            return None

    def sun(self):
        """
        Retrieves information regarding the sunset and sunrise according to UTC format.

        Returns:
            tuple or None: A tuple containing time of sunrise and sunset in UTC format.
        """
        result = self.make_request()
        if result:
            sun_query = result.get("sys")
            if sun_query:
                sunrise_query, sunset_query = sun_query["sunrise"], sun_query["sunset"]
                sunrise_obj, sunset_obj = datetime.utcfromtimestamp(sunrise_query), datetime.utcfromtimestamp(sunset_query)
                sunrise, sunset = sunrise_obj.strftime("%H:%M:%S UTC"), sunset_obj.strftime("%H:%M:%S UTC")
                return sunrise, sunset
            else:
                logging.error("Error getting sun information.")
        else:
            return None

# print(Weather("toroo").coordinates())