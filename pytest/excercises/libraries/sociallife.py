''' The script to find the  personal information'''

friend_list = ["Sandeep","Puneet","Bharat","Sachin","Alok"]
friend_info = {"Sandeep":"Prabhu",
                "Puneet":"Kumar",
                "Bharat":"Pai",
                "Sachin":"Singh",
                "Alok":"Rao" }

def find_friend(friend_name):
    ''' to check the friend name is in list or not'''
    if friend_name in friend_list:
        return True
    else:
        return False

def find_friend_surname(friend_surname):
    ''' to find the friends surname in dict'''
    if friend_surname in friend_info.keys():
        return friend_info[friend_surname]
    else:
        return False