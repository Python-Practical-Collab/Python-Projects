import os
import json
import requests

class Main():

    def __init__(self, query:str, pageNumber:int = 1):
        self.query = query
        self.pageNumber = pageNumber

    def movie_search(self):
        if self.query == "":
            return
        else: pass

        url = f"https://api.consumet.org/movies/viewasian/{self.query}?page={self.pageNumber}"
        response = requests.get(url).json()
        return response
        
    def movie_display(self):
        print("==========================")

        for i in self.movie_search()["results"]:
            
            for _ in i:
                print(f"Title: {i['title']}")
                print(f"ID: {i['id']}")
                print("==========================")
                break

        self.movie_input()

    def movie_input(self):
        name = input("Enter name of the series: ")
        x = self.movie_search()["results"]
        for i in x:
            for _ in i:
                if i["title"] == name:
                    print(True)
    

Main("vincenzo").movie_display()

