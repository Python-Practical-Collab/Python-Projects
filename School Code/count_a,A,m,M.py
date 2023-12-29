# Count "a", "A", "m", "M" from a text file

info = {
    "a": 0,
    "A": 0,
    "m": 0,
    "M": 0
}

def main():
    with open("temp/input.txt", "r") as file:
        data = [i for i in file.read()]

    print(f"Number of a: {data.count('a')}")
    print(f"Number of A: {data.count("A")}")
    print(f"Number of m: {data.count("m")}")
    print(f"Number of M: {data.count("M")}")

main()