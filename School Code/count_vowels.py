# Count number of vowels from a given text file

def main():
    with open("temp/input.txt", "r") as file:
        data = file.read().split()
        word_with_vowels = [word for word in data  if any(char in "aeiou" for char in word)]
        print(f"Number of vowels: {len(word_with_vowels)}")

main()