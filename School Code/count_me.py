# Program to count the occurances of the word "me" in a text file

def main():
    with open("temp/input.txt", "r") as file:
        data = file.read().split()
        me = [i for i in data if i == "me" or i == "Me"]
        print(f"Occurances of me: {me.count('me')}")

main()