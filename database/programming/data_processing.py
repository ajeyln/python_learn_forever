import sqlite3
import csv
import os

def create_table_list_dict(c, table_name, list_header):
    '''Creation of list of dictionaries from table'''
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
    '''Creation of list of dictionaries from lists'''
    list_dicti = []
    for i in range(0, len(list_values)):
        dict_row = {}
        for j in range(0, len(list_values[0])):
            dict_row[list_header[j]] = list_values[i][j]
        print(dict_row)
        list_dicti.append(dict_row)
    return list_dicti

def create_input_list(input_file):
    ''' Creation lists from list files '''
    input_list = []
    with open(f'input{os.path.sep}{input_file}', 'r') as input_data:
        for row in csv.reader(input_data):
            input_list.append(row)
    return input_list

def create_file(file_name, c, table_name, list_header):
    ''' Creation of files'''
    if os.path.exists(f"result{os.path.sep}{file_name}"): # removing the files if already exists
        os.remove(f"result{os.path.sep}{file_name}")
        
    with open(f'result{os.path.sep}{file_name}', 'a', newline='') as file_details:
        writer = csv.writer(file_details)
        writer.writerow(list_header)
        list_dict = create_table_list_dict(c, table_name, list_header)
        for k in range(0, len(list_dict)):
            print(list_dict[k].values())
            writer.writerow(list_dict[k].values())

if __name__ == "__main__":
    con = sqlite3.connect('school.db')
    c = con.cursor()
    table_name = "student"

    # List of Header Creation
    c.execute('PRAGMA table_info(student);')
    dummy_list_header = [list(x) for x in c.fetchall()]
    list_header = [dummy_list_header[y][1] for y in range(0, len(dummy_list_header))]

    # file creation before updation
    file_name = '01_student_info_before_updation.csv'
    create_file(file_name, c, table_name, list_header)

    # Inserting values
    input_insert_file = 'insert.csv'
    insert_line = create_input_list(input_insert_file)
    insert_file = [b for b in insert_line]

    for i in range(1, len(insert_file)):
        c.execute(f"insert into student values({insert_file[i][0]}, \'{insert_file[i][1]}', {insert_file[i][2]}, \'{insert_file[i][3]}', {insert_file[i][4]})")

    file_insert = '02_student_info_after_inserting.csv' # file creation before inserting
    create_file(file_insert, c, table_name, list_header)

    # Updating values
    input_update_file = 'update.csv'
    update_line = create_input_list(input_update_file)

    update_list_dict = create_list_dict(list_header, update_line)
    c.execute(f"UPDATE {table_name} SET NAME = \'{update_list_dict[1]['NAME']}' WHERE ID = {update_list_dict[1]['ID']};")

    file_update = '03_student_info_after_updation.csv' # # file creation before updation
    create_file(file_update, c, table_name, list_header)

    # Delete row
    input_delete_file = 'update.csv'
    delete_line = create_input_list(input_delete_file)

    delete_list_dict = create_list_dict(list_header, delete_line)
    c.execute(f"DELETE FROM {table_name} WHERE ID = {delete_list_dict[1]['ID']}")

    file_delete = '04_student_info_after_deletion.csv' # # file creation before deletion
    create_file(file_delete, c, table_name, list_header)
