''' In order to import custom files from libraries folder, we need to reach libraries folder from source folder'''
import sys
temp_list = str(__file__).split("/") # Spliting current folder path
temp_join = "/".join(temp_list[:-1]) # joining the file path except the current file
'''adding libraries folder path to the file path 
(as the libraries folder is above the current folder we need to add two dots)'''
temp_con = (temp_join + "/../libraries") 
sys.path.append(temp_con)

''' importing from custom files'''
from operation import add_num
from operation import sub_num
from operation import mul_num
from operation import div_num
from operation import odd_even
from helper import display_greeting
from helper import display_name

# This function will greets with your entered name and do the mathematical librariess
def oper_num():
    display_greeting()
    name_2 = input("Please Enter Your name:")
    display_name(name_2)
    print("Now we are going to start Mathematical librariess")
    value_1 = int(input("Please Enter a Number:"))
    value_2 = int(input("Please Enter another number:"))
    add_num(value_1,value_2)
    sub_num(value_1,value_2)
    mul_num(value_1,value_2)
    while(value_2 == 0): # The condition will execute while second is zero
        value_2 = int(input("Please Enter a number other than zero:"))
    else:
        print(div_num(value_1,value_2))
    odd_even(value_2)


if __name__ == '__main__':
    oper_num()
