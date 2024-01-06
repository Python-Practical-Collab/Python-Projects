'''
    Program to create a binary file with roll no., name and marks. also input a roll number and update the marks.
'''

import os
import pickle

def proceed():
    ask = input("Do you want to continue (y/n): ")
    match ask:
        case "y":
            menu()
        case "n", _:
            exit()

def write():
    name = input("Enter name: ")
    roll_no = int(input("Enter roll no: "))
    marks = int(input("Enter marks: "))
    with open("temp/students.dat", "ab") as file:
        pickle.dump([name, roll_no, marks], file)
    
    proceed()

def read():
    with open("temp/students.dat", "rb") as file:
        try:
            while True:
                loaded_data = pickle.load(file)
                print(loaded_data)
        except EOFError:
            pass
    
    proceed()

def update():
    roll_no = int(input("Enter the roll no. for which you'd like to update marks: "))
    updated_marks = int(input("Enter updated marks: "))
    with open("temp/students.dat", "rb+") as file:
        try:
            while True:
                record = pickle.load(file)
                if record[1] == roll_no:
                    record[2] = updated_marks  
                    print(record)

                    file.seek(file.tell() - pickle.dumps(record).__len__())
                    pickle.dump(record, file)
                    
                    file.seek(0, 2)
                    break
                else:
                    print("Record not found.")
        except EOFError:
            pass

    proceed()

def menu():
    os.system("cls")
    available_functions = {
        1: "View Records",
        2: "Add Records",
        3: "Update Records",
        4: "Exit"
    }

    print("Available functions are: ")
    for i, j in available_functions.items():
        print(f"{i}. {j}")
    
    user_choice = None
    while user_choice not in available_functions:
        user_choice = int(input("Enter your choice: "))

    match user_choice:
        case 1:
            read()
        case 2:
            write()
        case 3:
            update()
        case 4:
            exit()

if __name__ == "__main__":
    menu()