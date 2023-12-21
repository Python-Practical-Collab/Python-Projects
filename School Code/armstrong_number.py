# Armstrong Number - An Armstrong number (also known as a narcissistic number, pluperfect digital invariant, or pluperfect number) is a number that is the sum of its own digits each raised to the power of the number of digits. In other words, an n-digit number is an Armstrong number if the sum of its digits, each raised to the power of n, is equal to the number itself.

class Main:

    def __init__(self, number:str):
        self.number = number
        self.data = [int(i)**len(self.number) for i in self.number]

    def check_Armstrong(self):
        data2 = [int(i) for i in self.data]
        if sum(data2) == int(self.number):
            print(f"{self.number} is an armstrong number.")
        else:
            print(f"{self.number} is not an armstrong number.")

number = input("Enter your input(should be numerical): ")
if number.isdigit():
    Main(number).check_Armstrong()
else:
    print("Make sure that the input is correct.")