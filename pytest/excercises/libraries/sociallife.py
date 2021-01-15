''' The script to find the  personal information'''

friend_list = ["Sandeep","Puneet","Bharat","Sachin","Alok"]
friend_info = {"Sandeep":"Prabhu",
                "Puneet":"Kumar",
                "Bharat":"Pai",
                "Sachin":"Singh",
                "Alok":"Rao" }

def find_friend():
    ''' to check the friend name is in list or not'''
    friend_name = input("Enter a friends name: ")
    if friend_name in friend_list:
        return True
    else:
        return False

def find_friend_surname():
    ''' to find the friends surname in dict'''
    friend_surname = input("Enter a friends name: ")
    if friend_surname in friend_info.keys():
        return friend_info[friend_surname]
    else:
        return False

if __name__ == "__main__":
    print(find_friend())
    print(find_friend_surname())
