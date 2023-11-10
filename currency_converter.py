# Currency Converter

class Main:
    
    def __init__(self):
        self.currency = {
            "INR -> USD" : 0.012,
            "USD -> INR" : 83.27,
            "EURO -> INR" : 89.22,
            "INR -> EURO" : 0.011,
        }

    def check(self, initial1 = None, target1 = None):

        initial, target = initial1.upper(), target1.upper()

        check_string = f"{initial} -> {target}"

        for i in self.currency.keys():
            if i == check_string:
                found = True
                break
            else: found = False

        if found == False: 
            print("That currency was not found.")
            exit()
        else:
            self.convert(check_string)

    def convert(self, convert_query):
        print(f"Converting {convert_query}")

        curr = [element.strip() for element in convert_query.split("->")]
        values = [float(input(f"Enter amount in {curr[0]}: ")) for i in range(1)]

        print(f"{values[0]} {curr[0]} in {curr[1]} is {self.currency[convert_query] * values[0]} {curr[1]}")
 

def start():
    print("Welcome to Currency Converter!!")
    i_curr = input("Enter initial currency: ").upper()
    t_curr = input("Enter target currency: ").upper()

    Main().check(i_curr, t_curr)

start()