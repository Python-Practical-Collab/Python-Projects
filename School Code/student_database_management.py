'''
	Create a database management system to manage student records like name, roll number, marks in different subjects
	1. Add the ability to add, delete or modify student records.
	2. Allow users to retrive and display student details based on different records.

	My Approach:
		We will be creating two databases, one which will contain the basic details of the student and will check whether the student is studying in the institution or not. Second table will be used to fetch the marks of the student. Since, 2 students cannot have the same marks, we can use their roll no to store their corresponding marks in each subject.
'''

import os
import pandas as pd
import sqlite3 as sq
from tabulate import tabulate

connection = sq.connect("databases/students.db")
cursor = connection.cursor()

def create_database():
	"""
		This function only needs to run once and as expected it will create the database.
	"""
	cursor.execute(
		"""
		create table if not exists students(
			'Admission_Number' integer,
			Name varchar(30),
			Roll_No integer
		)
		"""
	)

	cursor.execute(
		"""
		create table if not exists marks(
			Roll_No integer,
			Maths integer,
			Physics integer
			Chemistry integer,
			English integer,
			CS integer,
			Total integer
		)
		"""
	)

def view_tables():
	tables_opted = None
	tables = {
				1: "students", 
				2: "marks"
			}

	while tables_opted is None or tables_opted not in tables.values():
		for i, j in tables.items():
			print(f"{i}. {j}")

		tables_opted = input("Plese choose: ")
		if tables_opted in ["1", "2"]:
			break

	if tables_opted in ["students", "1"]:
		os.system("cls")
		print("Info on Students")
		cursor.execute(
			"""
			select Roll_No, Name, Admission_Number from students order by Roll_No ASC;
			"""
		)
		rows = cursor.fetchall()
		columns = [desc[0] for desc in cursor.description]
		df = pd.DataFrame(rows, columns = columns)
		print(tabulate(df, headers = columns, tablefmt = 'pretty', showindex = 'never'))

	elif tables_opted in ["marks", "2"]:
		os.system("cls")
		print("""
		  Info on Marks
		""")
		cursor.execute(
			"""
			select * from marks order by Roll_No ASC;
			"""
		)
		rows = cursor.fetchall()
		columns = [desc[0] for desc in cursor.description]
		df = pd.DataFrame(rows, columns = columns)
		print(tabulate(df, headers = columns, tablefmt = 'pretty', showindex = 'never'))

def student_entry():
	data = {
		"admission_no": "",
		"name": "",
		"roll_no": ""
	}
	
	for i in data.keys():
		data[i] = input(f"Enter {i}: ") 

	cursor.execute(
		f"""
		insert into students (Admission_Number, Name, Roll_No) VALUES ({int(data['admission_no'])}, '{data['name']}', {int(data['roll_no'])})
		""")
	connection.commit()

def marks_entry():
	data = {
		"roll_no": "",
		"maths": "",
		"physics": "",
		"chemistry": "",
		"english": "",
		"cs": "",
	}

	for i in data.keys():
		if i == "roll_no":
			data[i] = input(f"Enter {i}: ")
		else:
			data[i] = input(f"Enter marks in {i}: ")

	cursor.execute(
		"""
		select Roll_No from marks
		"""
	)
	rows = cursor.fetchall()
	if data["roll_no"] in rows:
		print("Entry for that roll no was already found in our records.")
		exit()
	else: pass

	total_marks = [int(i) for i in data.values() if i != data["roll_no"]]

	cursor.execute(
		f"""
		insert into marks (Roll_No, Maths, Physics, English, CS, Total) VALUES ({data["roll_no"]}, {data["maths"]}, {data['physics']}, {data['chemistry']}, {data['english']}, {data["cs"]}, {total_marks})
		"""
	)

def main():
	available_functions = {
		1: "View Database",
		2: "Add Student info",
		3: "Add student marks",
		4: "Exit"
	}

	user_input = None
	while user_input not in available_functions:
		user_input = int(input("Here: "))
	print(user_input)

main()