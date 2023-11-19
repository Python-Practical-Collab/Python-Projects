# Currency Converter
import forex_python.converter as CurrencyRates

class Main:
    
    def convert(self, inCurr, outCurr, values:float = None): # type: ignore

        if inCurr == "" or outCurr == "":
            return "Please provide some values."
        else: pass

        try:
            rates = CurrencyRates.get_rate(inCurr, outCurr)
        except CurrencyRates.RatesNotAvailableError as e:
            print(f"Error: {e}")
            return "Please make sure that the currencies are right."
        
        if values is None:
            values = float(input(f"Enter amount in {inCurr}: "))
        else:
            pass

        return (f"{values} {inCurr} is {round(rates * values, 2)} {outCurr}") # type: ignore

def start():
    print("Welcome to Currency Converter!!")
    i_curr = input("Enter initial currency: ").upper()
    t_curr = input("Enter target currency: ").upper()

    print(Main().convert(i_curr, t_curr))

if __name__ == "__main__":
    start()