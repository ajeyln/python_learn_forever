''' to covert csv file from list of dictionaries'''
import csv
import os

# pylint: disable=line-too-long
list_dict = [{'ID':2019102, 'NAME':'Ananth', 'AGE': 6, 'SEX':'Male', 'GRADE': 1},
            ]
# pylint: enable=line-too-long

list_key = []
for header_name in list_dict[0]:
    list_key.append(header_name) # Header creation

if os.path.exists("update.csv"): # removing the files if already exists
    os.remove("update.csv")

# pylint: disable=consider-using-enumerate
with open('update.csv', 'a', newline='') as file: # creating .csv file
    writer = csv.writer(file)
    writer.writerow(list_key)
    for i in range(0, len(list_dict)): # adding the vales to the file
        print(list_dict[i].values())
        writer.writerow(list_dict[i].values())
