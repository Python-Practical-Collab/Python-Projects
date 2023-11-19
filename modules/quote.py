import requests
import logging

class Quote:
    """
    A class to fetch quotes, daily quotes and random quotes from zenquotes API

    Parameters:
        No parameters are required, as API key is not required to use their service

    Attributes:
        fif (str): The endpoint to fetch 50 random quotes from the API 
        random (str): The endpoint to fetch 1 random quote from the API
        day (str): The endpoint to fetch the quote of the day from the API
    """

    def __init__(self) -> None:
        """
        Initialized the Weather class.

        Parameters:
            None are required.
        """
        self.fif = "https://zenquotes.io/api/quotes"
        self.random = "https://zenquotes.io/api/random"
        self.day = "https://zenquotes.io/api/today"

        logging.basicConfig(level=logging.INFO)


    def random_quote(self, *kwargs):
        """
        Fetches a random quote from the API

        Returns:
            tuple or None: A tuple containing quote and author's name
        """
        if kwargs: 
            logging.error(f"Please refrain from passing any unnecessary parameters {kwargs}.")

        try:
            response = requests.get(self.random)
            return response.json()[0]["q"].strip(), response.json()[0]["a"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")  
            return None
        
    def quote_of_day(self, *kwargs):
        """
        Fetches the quote of the day from the API (Remains same throughout the day)

        Returns:
            tuple or None: A tuple containing quote and author's name
        """
        if kwargs: 
            logging.error(f"Please refrain from passing any unnecessary parameters {kwargs}.")

        try:
            response = requests.get(self.day)
            return response.json()[0]["q"], response.json()[0]["a"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")

    def random_quotes(self, amount:int = 2, *kwargs) -> dict:  # type: ignore
        """
        Fetches 50 random quotes from the API but returns only a specific amount of quotes

        Parameters:
            amount (int): An optional parameter to specify the number of quotes to display. Defaults to 2
        Returns:
            dict or None: A dictionary having quotes and their author in key, value pair. 
        """
        if kwargs:
            logging.error(f"Please refrain from passing any unnecessary parameters {kwargs}.")
        if amount > 50: amount = 50
        
        try:
            response = requests.get(self.fif)
            quotes = {response.json()[i]["q"] : response.json()[i]["a"] for i in range(amount)}
            return quotes
        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")