units = {
    "m to cm": 100,
    "cm to m": 0.01,
    "kg to g": 1000,
    "g to kg": 0.001,
    "m to mm": 1000,
    "mm to m": 0.001,
    "l to ml": 1000,
    "ml to l": 0.001,
    "miles to km": 1.60934,
    "km to miles": 0.621371,
    "inches to cm": 2.54,
    "cm to inches": 0.393701,
    "pounds to kg": 0.453592,
    "kg to pounds": 2.20462,
    "feet to meters": 0.3048,
    "meters to feet": 3.28084,
    "yards to meters": 0.9144,
    "meters to yards": 1.09361,
    "ounces to grams": 28.3495,
    "grams to ounces": 0.03527396,
    "gallons to liters": 3.78541,
    "liters to gallons": 0.264172,
    "hours to minutes": 60,
    "minutes to hours": 1/60,
    "days to hours": 24,
    "hours to days": 1/24
}

def start():
    convert_q1, convert_q2 = input("From: "), input("To: ")
    convert_query = f"{convert_q1} to {convert_q2}"
    if convert_query in units.keys():
        values = units[convert_query]
        amount = int(input('Enter numerical value: '))
        return f"{amount} {convert_q1} is {round(amount * values, 2)} {convert_q2}"
    else:
        print("Units not found.")
        exit()

print(start())