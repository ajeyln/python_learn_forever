''' The script to find the  personal information'''
import sys
from io import StringIO

friend_info = {"Sandeep":"Prabhu",
                "Puneet":"Kumar",
                "Bharat":"Pai",
                "Sachin":"Singh",
                "Alok":"Rao" }
PERSON_INFO = {'Name':'Ajeya', "Surname" : "Nayak"}
PERSON_DET = {'Name':'Sachin', "Surname" : "Singh"}

def find_friend_surname():
    ''' to find the friends surname in dict'''
    friend_name = input("Enter the name:")
    print(friend_name)
    if friend_name in friend_info.keys():
        return friend_info[friend_name]
    else:
        return False

def mod_info_dict(config=None):
    '''to find person info'''
    return f"Name={PERSON_INFO['Name']}; Surname={PERSON_INFO['Surname']};"

def del_info_dict(config=None):
    '''to find person info'''
    return f"Name={PERSON_DET['Name']}; Surname={PERSON_DET['Surname']};"
