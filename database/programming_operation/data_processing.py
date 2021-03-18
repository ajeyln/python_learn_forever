import sqlite3
import csv
import os

def head_file(database_name, table_name, insert_file, update_file, delete_file):
    ''' Data processing methods'''
    cur_val = connect_database(database_name) # Connecting database
    list_header = get_header(cur_val, table_name) # Getting Header List
    create_file('01_student_info_before_updation.csv', cur_val, table_name, list_header) # File creation before updation
    insert_entry = insert_value(cur_val, insert_file) # Inserting values
    create_file('02_student_info_after_inserting.csv', cur_val, table_name, list_header)
    update_entry = update_value(cur_val, list_header, table_name, update_file) # Updating value
    create_file('03_student_info_after_updation.csv', cur_val, table_name, list_header)
    delete_entry = delete_value(cur_val, table_name, list_header, delete_file) # Deleting values
    create_file('04_student_info_after_deletion.csv', cur_val, table_name, list_header)

def connect_database(database_name):
    '''this function is used for connecting database'''
    con_db = sqlite3.connect(f'{database_name}')
    cur_val = con_db.cursor()
    return cur_val

def get_header(cur_val, table_name):
    '''List of Header Creation'''
    cur_val.execute(f'PRAGMA table_info({table_name})')
    dummy_list_header = [list(x) for x in cur_val.fetchall()]
    list_header = [dummy_list_header[y][1] for y in range(0, len(dummy_list_header))]
    return list_header

def insert_value(cur_val, input_insert_file):
    '''Inserting values to table'''
    insert_line = create_input_list(input_insert_file)
    insert_file = [b for b in insert_line]
    for i in range(1, len(insert_file)):
        cur_val.execute(f"insert into student values \
            ({insert_file[i][0]}, \'{insert_file[i][1]}', {insert_file[i][2]}, \'{insert_file[i][3]}', {insert_file[i][4]})")

def update_value(cur_val, list_header, table_name, input_update_file):
    '''Updating values to table'''
    update_line = create_input_list(input_update_file)
    update_list_dict = create_list_dict(list_header, update_line)
    cur_val.execute(f"UPDATE {table_name} SET NAME \
        = \'{update_list_dict[1]['NAME']}' WHERE ID = {update_list_dict[1]['ID']};")

def delete_value(cur_val, table_name, list_header, input_delete_file):
    delete_line = create_input_list(input_delete_file)
    delete_list_dict = create_list_dict(list_header, delete_line)
    cur_val.execute(f"DELETE FROM {table_name} WHERE ID = {delete_list_dict[1]['ID']}")

def create_table_list_dict(cur_val, table_name, list_header):
    '''Creation of list of dictionaries from table'''
    cur_val.execute(f"Select * from {table_name}")
    list_values = [list(z) for z in cur_val.fetchall()]
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

def create_file(file_name, cur_val, table_name, list_header):
    ''' Creation of files'''
    if os.path.exists(f"result{os.path.sep}{file_name}"): # removing the files if already exists
        os.remove(f"result{os.path.sep}{file_name}")
        
    with open(f'result{os.path.sep}{file_name}', 'a', newline='') as file_details:
        writer = csv.writer(file_details)
        writer.writerow(list_header)
        list_dict = create_table_list_dict(cur_val, table_name, list_header)
        for k in range(0, len(list_dict)):
            print(list_dict[k].values())
            writer.writerow(list_dict[k].values())

if __name__ == "__main__":
    head_file('school.db', 'student', 'insert.csv', 'update.csv', 'delete.csv')
