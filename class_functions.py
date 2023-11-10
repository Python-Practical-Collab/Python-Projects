# class function

class Human: 

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking.")
    
    def breathe(self):
        print(f"{self.name} is breathing.")

class Adult(Human):

    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender

    def earn(self):
        print(f"{self.name} is earning.")

    def what_gender(self):
        print(f"{self.name} is {self.gender}")

h = Adult("PQR", "Female")
h.what_gender()