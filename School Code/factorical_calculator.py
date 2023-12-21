# Factorial Calculator -  The term "factorial" refers to the product of all positive integers up to a given number. It is denoted by the exclamation mark (!).

class Main:

    def __init__(self, number:int):
        self.number = number


    def calculator(self):
        a = 1
        for i in range(1, self.number+1):
            a = a*i
        print(f"The value of {self.number}! is {a}")
    
Main(10).calculator()