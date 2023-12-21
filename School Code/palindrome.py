# Palindrome - A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). In other words, it remains unchanged when its characters are reversed.

class Main:

    def __init__(self, query):
        self.condition = []
        self.query = query
        self.data = [i for i in self.query]
    
    def check_palindrome(self):
        data_2 = [self.data[-i] for i, j in enumerate(self.data, start=1)]
        if self.data == data_2:
            print(f"{self.query} is a palindrome.")
        else: print(f"{self.query} is not a palindrome.")

Main(input("Enter word: ").lower()).check_palindrome()