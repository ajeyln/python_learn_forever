''' The script to find the  personal information'''
import sys
from io import StringIO

friend_info = {"Sandeep":"Prabhu",
                "Puneet":"Kumar",
                "Bharat":"Pai",
                "Sachin":"Singh",
                "Alok":"Rao" }

def find_friend_surname():
    ''' to find the friends surname in dict'''
    friend_name = input("Enter the name:")
    print(friend_name)
    if friend_name in friend_info.keys():
        return friend_info[friend_name]
    else:
        return False
