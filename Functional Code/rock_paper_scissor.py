# Rock Paper Scissor 

import os
import random

class Main:

    def __init__(self, user:str) -> None:
        self.user = user
        self.choices = ["Rock", "Paper", "Scissor"]
        self.computer = random.choice(self.choices)

    def game(self):
        if self.user == self.computer:
            print("Game Tied!!")
        # if computer wins
        elif (self.computer == "Rock" and self.user == "Scissor") or (self.computer == "Paper" and self.user == "Rock") or (self.computer == "Scissor" and self.user == "Paper"):
            print(f"Computer won by choosing {self.computer}\nUser chose: {self.user}")
        else:
            print(f"User won by choosing {self.user}\nComputer chose: {self.computer}")
        
def start():
    os.system("clear")
    user_choice = input("Enter your choice: ").capitalize()
    if user_choice not in ["Rock", "Paper", "Scissor"]:
        print("Your input was not right!")
        exit()
    else:
        Main(user_choice).game()

start()
    