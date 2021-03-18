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

def create_table_list_dict(c, table_name, list_header):
    '''Creation of list of dictionaries'''
    c.execute(f"Select * from {table_name}")
    list_values = [list(z) for z in c.fetchall()]
    list_table_dicti = []
    for i in range(0, len(list_values)):
        dict_row = {}
        for j in range(0, len(list_values[0])):
            dict_row[list_header[j]] = list_values[i][j]
        print(dict_row)
        list_table_dicti.append(dict_row)
    return list_table_dicti

def create_list_dict(list_header, list_values):
    '''Creation of list of dictionaries'''
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

    if os.path.exists(f"result{os.path.sep}01_student_info_before_updation.csv"): # removing the files if already exists
        os.remove(f"result{os.path.sep}01_student_info_before_updation.csv")

    with open(f'result{os.path.sep}01_student_info_before_updation.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list_header)
        list_dict = create_table_list_dict(c, table_name, list_header)
        for k in range(0, len(list_dict)):
            print(list_dict[k].values())
            writer.writerow(list_dict[k].values())

    # Inserting values
    insert_line = []
    with open(f'input{os.path.sep}insert.csv', "r") as insert_data:
        for line in csv.reader(insert_data):
            insert_line.append(line)

    insert_file = [b for b in insert_line]

    for i in range(1, len(insert_file)):
        c.execute(f"insert into student values({insert_file[i][0]}, \'{insert_file[i][1]}', {insert_file[i][2]}, \'{insert_file[i][3]}', {insert_file[i][4]})")

    if os.path.exists(f'result{os.path.sep}02_student_info_after_inserting.csv'): # removing the files if already exists
        os.remove(f'result{os.path.sep}02_student_info_after_inserting.csv')

    with open(f'result{os.path.sep}02_student_info_after_inserting.csv', 'a', newline='') as after_insert:
        writer = csv.writer(after_insert)
        writer.writerow(list_header)
        list_insert = create_table_list_dict(c, table_name, list_header)
        for k in range(0, len(list_insert)):
            print(list_insert[k].values())
            writer.writerow(list_insert[k].values())

    # Updating values
    update_line = []
    with open(f'input{os.path.sep}update.csv', 'r') as update_data:
        for row in csv.reader(update_data):
            update_line.append(row)
        update_list_dict = create_list_dict(list_header, update_line)
        c.execute(f"UPDATE {table_name} SET NAME = \'{update_list_dict[1]['NAME']}' WHERE ID = {update_list_dict[1]['ID']};")

    if os.path.exists(f'result{os.path.sep}03_student_info_after_updation.csv'):
        os.remove(f'result{os.path.sep}03_student_info_after_updation.csv')

    with open(f'result{os.path.sep}03_student_info_after_updation.csv', 'a', newline='') as after_update:
        writer = csv.writer(after_update)
        writer.writerow(list_header)
        list_update = create_table_list_dict(c, table_name, list_header)
        for k in range(0, len(list_update)):
            print(list_update[k].values())
            writer.writerow(list_update[k].values())

    # Delete row
    delete_line = []
    with open(f'input{os.path.sep}delete.csv', 'r') as delete_data:
        for queue in csv.reader(delete_data):
            delete_line.append(queue)
        delete_list_dict = create_list_dict(list_header, delete_line)
        c.execute(f"DELETE FROM {table_name} WHERE ID = {delete_list_dict[1]['ID']}")

    if os.path.exists(f'result{os.path.sep}04_student_info_after_deletion.csv'):
        os.remove(f'result{os.path.sep}04_student_info_after_deletion.csv')

    with open(f'result{os.path.sep}04_student_info_after_deletion.csv', 'a', newline='') as after_delete:
        writer = csv.writer(after_delete)
        writer.writerow(list_header)
        list_delete = create_table_list_dict(c, table_name, list_header)
        for k in range(0, len(list_delete)):
            print(list_delete[k].values())
            writer.writerow(list_delete[k].values())
