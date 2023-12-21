# Fibanocci Series - The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

class Main:

    def __init__(self, range):
        self.range = range
        self.series = [0, 1]

    def logic(self):
        for _ in range(self.range):
            self.series.append(self.series[-1] + self.series[-2])

        print(f"Fibanocci Series with {self.range + 2} elements is: ")
        print(self.series)

Main(int(input("Enter limit: "))).logic()