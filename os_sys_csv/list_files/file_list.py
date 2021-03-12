''' to find the list of directory and file paths'''
from glob import glob
import os

# Designating path
designated_path = os.getcwd()

# Empty list of file paths
file_paths = []

for x in os.walk(designated_path):
    folder_path = glob(x[0]) # to find the path of the folder paths
    file_paths.append(folder_path)
    for file_name in glob(os.path.join(x[0], '*.*')):#to find the path of the files paths
        file_paths.append(file_name)

# Creating file and adding path details in it
file_detail = open('fullpath.txt', "a")
for file_path in file_paths:
    file_detail.write(f"{file_path} \n")
file_detail.close()
