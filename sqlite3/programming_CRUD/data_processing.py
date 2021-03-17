import sqlite3
import csv
import os

con = sqlite3.connect('school.db')

c = con.cursor()

# List of Header Creation
c.execute('PRAGMA table_info(student);')

dummy_list_header = []
for x in c.fetchall():
    dummy_list_header.append(list(x))

list_header = []
for y in range(0, len(dummy_list_header)):
    list_header.append(dummy_list_header[y][1])
print(list_header)

# List of values creation
list_values = []

c.execute("Select * from student")

for z in c.fetchall():
    list_value = list(z)
    list_values.append(list_value)

print((list_values))

# Creation of list of dictionaries
list_dict = []
dict_row = {}
for i in range(0, len(list_values)):
    for j in range(0, len(list_values[0])):
        dict_row[list_header[j]] = list_values[i][j]
    print(dict_row)
    list_dict.append(dict_row)
print(list_dict)

if os.path.exists("student_info_before_updation.csv"): # removing the files if already exists
    os.remove("student_info_before_updation.csv")

with open('student_info_before_updation.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list_header)
    for k in range(0, len(list_dict)):
        print(list_dict[k].values())
        writer.writerow(list_dict[k].values())

insert_file=[]
with open('insert.csv','r') as insert:
    for line in csv.reader(insert):
        insert_file.append(line)
    print(insert_file)