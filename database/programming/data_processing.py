import sqlite3
import csv
import os

'''
con = sqlite3.connect('school.db')
c = con.cursor()
table_name = "student"

# List of Header Creation
c.execute('PRAGMA table_info(student);')
dummy_list_header = [list(x) for x in c.fetchall()]
list_header = [dummy_list_header[y][1] for y in range(0, len(dummy_list_header))]
'''

def create_list_dict(c, table_name, list_header):
    '''Creation of list of dictionaries'''
    c.execute(f"Select * from {table_name}")
    list_values = [list(z) for z in c.fetchall()]
    list_dicti = []
    for i in range(0, len(list_values)):
        dict_row = {}
        for j in range(0, len(list_values[0])):
            dict_row[list_header[j]] = list_values[i][j]
        print(dict_row)
        list_dicti.append(dict_row)
    return list_dicti

if __name__ == "__main__":
    con = sqlite3.connect('school.db')
    c = con.cursor()
    table_name = "student"

    # List of Header Creation
    c.execute('PRAGMA table_info(student);')
    dummy_list_header = [list(x) for x in c.fetchall()]
    list_header = [dummy_list_header[y][1] for y in range(0, len(dummy_list_header))]

    if os.path.exists("student_info_before_updation.csv"): # removing the files if already exists
        os.remove("student_info_before_updation.csv")

    with open('student_info_before_updation.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list_header)
        list_dict = create_list_dict(c, table_name, list_header)
        print(list_dict)
        for k in range(0, len(list_dict)):
            print(list_dict[k].values())
            writer.writerow(list_dict[k].values())

    # Inserting values
    insert_line = []
    with open('insert.csv', "r") as insert_data:
        for line in csv.reader(insert_data):
            insert_line.append(line)

    insert_file = [b for b in insert_line]

    for i in range(1, len(insert_file)):
        c.execute(f"insert into student values({insert_file[i][0]}, \'{insert_file[i][1]}', {insert_file[i][2]}, \'{insert_file[i][3]}', {insert_file[i][4]})")

    if os.path.exists("student_info_after_inserting.csv"): # removing the files if already exists
        os.remove("student_info_after_inserting.csv")

    with open('student_info_after_inserting.csv', 'a', newline='') as after_insert:
        writer = csv.writer(after_insert)
        writer.writerow(list_header)
        list_insert = create_list_dict(c, table_name, list_header)
        for k in range(0, len(list_insert)):
            print(list_insert[k].values())
            writer.writerow(list_insert[k].values())
    
    # Updating values
    update_line = []
    