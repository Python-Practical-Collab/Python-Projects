import unittest
import sys
sys.path.append("/mnt/Work/Python/Projects/modules/")
from weather import Weather  # type: ignore

class TestWeather(unittest.TestCase):

    def test_valid_city(self):
        weather_instance = Weather("Toronto")
        result = weather_instance.make_request()
        self.assertIsNotNone(result, "Weather data should be available for a valid city.")
        if result:  # Only proceed if result is not None
            self.assertIsNotNone(weather_instance.coordinates(), "Coordinates should be available for a valid city.")
            self.assertIsNotNone(weather_instance.temperature(), "Temperature data should be available for a valid city.")
            self.assertIsNotNone(weather_instance.wind(), "Wind data should be available for a valid city.")
            self.assertIsNotNone(weather_instance.weather(), "Weather data should be available for a valid city.")
            self.assertIsNotNone(weather_instance.sun(), "Sun data should be available for a valid city.")

    def test_invalid_city(self):
        weather_instance = Weather("wfu iwehfihwf")
        result = weather_instance.make_request()
        self.assertIsNone(result, "Weather data should be None for an invalid city.")
        if result is None:  # Only proceed if result is None
            self.assertIsNone(weather_instance.coordinates(), "Coordinates should be None for an invalid city.")
            self.assertIsNone(weather_instance.temperature(), "Temperature data should be None for an invalid city.")
            self.assertIsNone(weather_instance.wind(), "Wind data should be None for an invalid city.")
            self.assertIsNone(weather_instance.weather(), "Weather data should be None for an invalid city.")
            self.assertIsNone(weather_instance.sun(), "Sun data should be None for an invalid city.")

if __name__ == '__main__':
    unittest.main()

# this is just a small test whether the live share is working as intended or not