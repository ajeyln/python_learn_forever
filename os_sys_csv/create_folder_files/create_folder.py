'''creating folder and moving the files after segregation'''
import os
import math
import shutil

# creating the folder before creating files
current_path = f'{os.getcwd()}{os.path.sep}result{os.path.sep}'

# Delting the folder if already exists
if os.path.isdir(current_path):
    shutil.rmtree(current_path)

# Creating the folder or making a new folder after existing folder got deleted
os.mkdir(current_path)

# creating files from 1 to 50
for i in range(1,50):
    new_folder = str(f'{math.floor(i/10)}')
    path_name = os.path.join(current_path, new_folder)
    if os.path.isdir(path_name): # checking whether folder are created or not
        file_name = f'{i}.txt'
        open(file_name, 'wb')
        shutil.move(file_name, path_name)
    else:
        os.mkdir(path_name)
        file_name = f'{i}.txt'
        open(file_name, 'wb')
        shutil.move(file_name, path_name)
