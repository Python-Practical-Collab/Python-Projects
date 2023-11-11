# Prime Number - A number which only has 1 and the number itself as its factor

class Main:
    
    def __init__(self, number:int):
        self.number = number
        self.condtion = True

    def check_prime(self):
        if self.number < 2:
            print(f"{self.number} should be greater than 2.")

        else:
            for i in range(2, self.number):
                if self.number % i == 0:
                    self.condtion = False
                    break
                else:
                    self.condtion = True
        
        print(f"{self.number} is a prime number" if self.condtion == True else f"{self.number} is not a prime number.")

Main(int(input("Enter number: "))).check_prime()