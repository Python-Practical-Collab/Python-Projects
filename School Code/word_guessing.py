import json
import random

"""
    Alternate method to get the words:
        words_request = requests.get(url = "https://www.randomlists.com/data/words.json").json()
        word_data = [value for value in words_request.values()]
    
    OR

        words = [value for value in requests.get(url = "https://www.randomlists.com/data/words.json").json().values()][0]
    
    But here, I have already stored the words in a json file therefore we don't need to make any requests to the API.
"""

def random_word():
    """
        Reading the json file to get the words then using the random module to choose a random word.

        Returns:
            str: A string containing random word from the json file

        Note: 
            1. You can refactor the below code as: 
                with open("test.json", "r") as file:
                    random_word = random.choice([value for value in (json.load(file).values())][0])
            2. This program works only for words with single occurance of each letter. I don't how to handle words with multiple occurance of one character. I have written a logic below to make sure that only those specific words are chosen.
    """

    with open("test.json", "r") as file:
        data = json.load(file)
        words = [value for value in data.values()][0]
        word = random.choice(words)

    """    
        non_repeat = [False if word.count(i) > 1 else True for i in word]
        while False in non_repeat:
            word = random.choice(words)
            non_repeat = [False if word.count(i) > 1 else True for i in word]
    """    

    while any(word.count(i) > 1 for i in word):
        word = random.choice(words)
    return word

counts = 0
word = random_word()
test = ["_"] * len(word) # this will create a list with n number of "_" in it, where n is the length of the actual word

def main():
    global counts

    while "_" in test:
        counts += 1
        try:
            word_guess = input("Enter your guess: ")[0]
        except IndexError:
            continue
        
        if word_guess not in word or word_guess in test or word_guess == "":
            print("Invalid guess. Try again.")
            continue
        
        print("Yayiee!! Correct guess!")

        test[word.index(word_guess)] = word_guess
        print(test)
        
main()
print(f"You guessed the correct word in {counts} tries.")