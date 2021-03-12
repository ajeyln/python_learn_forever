''' the scripts which converts csv file to list of dictionaries'''
import csv

FILE_NAME="baseball_players.csv"

list_file = []
list_row = []
list_dict = []

with open(FILE_NAME,'r') as data:
    for line in csv.reader(data):
        list_file.append(line)

# we need separate Head and other rows
header_list = list_file[0] # list of headers

for i in range(1, len(list_file)-1):
    list_row.append(list_file[i]) # List of other rows

# pylint: disable=consider-using-enumerate
for j in range(0, len(list_row)):
    dict_row = {}
    # pylint: disable=consider-using-enumerate
    for k in range(0, len(list_row[0])):
        dict_row[header_list[k]] = list_row[j][k] # creating dictionary
    list_dict.append(dict_row) # adding dictionary to list

for m in list_dict:
    print(m)
