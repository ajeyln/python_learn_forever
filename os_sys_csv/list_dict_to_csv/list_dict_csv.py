''' to covert csv file from list of dictionaries'''
import csv
import os

# pylint: disable=line-too-long
list_dict = [{"Searial_No": "1", "Female_Name": "Mary", "Husband_Name": "James", "Surname": "Smith", "Postal_Code": "210", "Place_Name": "Portsmouth", "State": "New Hampshire"},
            {"Searial_No": "2", "Female_Name": "Patricia", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "211", "Place_Name": "Portsmouth", "State": "New Hampshire"},
            {"Searial_No": "3", "Female_Name": "Linda", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "212", "Place_Name": "Portsmouth", "State": "New Hampshire"},
            {"Searial_No": "4", "Female_Name": "Barbara", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "213", "Place_Name": "Portsmouth", "State": "New Hampshire"},
            {"Searial_No": "5", "Female_Name": "Elizabeth", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "214", "Place_Name": "Portsmouth", "State": "New Hampshire"},
            {"Searial_No": "6", "Female_Name": "Jennifer", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "215", "Place_Name": "Portsmouth", "State": "New Hampshire"},
            {"Searial_No": "7", "Female_Name": "Maria", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "401", "Place_Name": "Pleasantville", "State": "New York"},
            {"Searial_No": "8", "Female_Name": "Susan", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "501", "Place_Name": "Holtsville", "State": "New York"},
            {"Searial_No": "9", "Female_Name": "Margaret", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "544", "Place_Name": "Holtsville", "State": "New York"},
            {"Searial_No": "10", "Female_Name": "Dorothy", "Husband_Name": "John", "Surname": "Johnson", "Postal_Code": "1001", "Place_Name": "Agawam", "State": "Massachusetts"}]
# pylint: enable=line-too-long

list_key = []
for dict in list_dict[0]:
    list_key.append(dict) # Header creation

if os.path.exists("pesonal_info.csv"): # removing the files if already exists
  os.remove("pesonal_info.csv")

with open('pesonal_info.csv', 'a', newline='') as file: # creating .csv file
    writer = csv.writer(file)
    writer.writerow(list_key)
    for i in range(0, len(list_dict)): # adding the vales to the file
        print(list_dict[i].values())
        writer.writerow(list_dict[i].values())
