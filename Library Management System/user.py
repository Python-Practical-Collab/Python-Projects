# User : Handles all the user related query i.e. returning, borrowing etc.
"""
    - User should be able to see book_info.db
    - User should NOT be able to see borrowed_books.db
    - User should authenticate themselves with a user id <firstname>_<secondname>@<admission number>
"""

import re

class User:

    """
        Represents a user with valid user id. The format for the username is checked via regex expression. Format should match <first-name>_<surname>@<admission-number>
    """

    pattern = re.compile(r'^[a-zA-Z]+_[a-zA-Z]+@\d+$')

    def __init__(self, userid):
        self.userid = userid
        self.check()

    def check_userid(self):
        """
            Checks whether the username is valid or not. Utilizes the above regex pattern.
            
            Returns:
                True: if the username is valid
                False: if the username is invalid
        """

        if self.pattern.match(self.userid):
            return True
        else:
            return False

    def check(self):
        """
            Utilizes the output of the check_user() function to validate the username. 
        """
        
        if self.check_userid():
            print("Username Validated.")
        else:
            print("Apologies but that username was not found.")
            exit()


user_id = input("Enter user id ( <firstname>_<secondname>@<admission number> ): ")
u = User(user_id)