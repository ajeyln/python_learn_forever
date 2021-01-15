# to check person information

PERSON_INFO = {'Name':'Ajeya', "Surname" : "Nayak"}
PERSON_DET = {'Name':'Sachin', "Surname" : "Singh"}

def mod_info_dict(config=None):
    return f"Name={PERSON_INFO['Name']}; Surname={PERSON_INFO['Surname']};"

def del_info_dict(config=None):
    return f"Name={PERSON_DET['Name']}; Surname={PERSON_DET['Surname']};"
