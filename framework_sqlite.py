# Framework program using sqlite database

import sqlite3

conn = sqlite3.connect("Framework.db")
cursor = conn.cursor()
config_table = 'fwconfig'
data_table = cursor.execute(f"select value from {config_table} where key = ?", ("title",)).fetchone()
data_table = data_table[0]

field_names = cursor.execute(f"PRAGMA table_info({data_table})").fetchall()
field_names	 = [data[1] for data in field_names]

def Create_record():
	data = []
	for field in field_names:
		data.append(input(f"Enter the {field}: "))
	data = tuple(data)
	cursor.execute(f"INSERT into {data_table} values {str(data)}")

def read_records():
	data = cursor.execute(f"select * from {data_table}").fetchall()
	if data:
		for record in data:
			print(record)
	else:
		print("No data found")

def update_record():
	record_id = input(f"Enter {field_names[0]} to update: ")
	for index in range(1, len(field_names)):
		print(f"{index}. Update {field_names[index]}")
	choice = int(input("enter your choice to update: "))
	cursor.execute(f"update {data_table} set {field_names[choice]} = ? where {field_names[0]} = ?",(input(f"Enter new {field_names[choice]}: "), record_id))

def delete_record():
	record_id = input(f"Enter {field_names[0]} to delete: ")
	cursor.execute(f"delete from {data_table} where {field_names[0]} = ?", (record_id,))

def ShowMenu():
	data = cursor.execute(f"SELECT * FROM {config_table} WHERE key = 'Menu'").fetchone()
	data = eval(data[1])
	for record in data:
		print(record)

while True:
	ShowMenu()
	Menu = [Create_record, read_records, update_record, delete_record, exit]
	Menu[int(input("Enter your choice: ")) - 1]()
	conn.commit()