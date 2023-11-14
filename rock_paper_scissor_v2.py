# Rock Paper Scissor - Abandoned

import os
import random

class Main:

    def __init__(self, rounds:int) -> None:
        self.choices = ["Rock", "Paper", "Scissor"]
        self.attempt = 0
        self.user = None
        self.user_options = []
        self.computer_options = []
        self.rounds = rounds


    def game(self):

        while self.attempt < self.rounds:

            self.computer = random.choice(self.choices)
            self.computer_options.append(self.computer)

            while self.user not in self.choices:
                self.user = input("Enter your choice(Rock, Paper or Scissor): ").capitalize()            
                self.user_options.append(self.user)
                self.attempt += 1

            self.user = None

        self.result()

    def result(self): # True -> User wins False -> Computer wins
        results = []
        print(f"Computer: {self.computer_options}")
        print(self.user_options)
        for i in self.computer_options:
            for j in self.user_options:
                if i == j:
                    results.append(None)
                    break
                # computer wins 
                elif (i == "Rock" and j == "Scissor") or (i == "Paper" and j == "Rock") or (i == "Scissor" and j == "Paper"):
                    results.append(False)
                    break
                # user wins
                else:
                    results.append(True)
                    break
        
        true = results.count(True)
        false = results.count(False)
        none = results.count(None)

        print(results)
        print(true, false, none)


def start():
    os.system("clear")
    try:
        user_choice = int(input("How many rounds: "))
    except ValueError as v:
        print(f"Please enter numeric values only.")
        exit()
    Main(user_choice).game()
    
start()
    