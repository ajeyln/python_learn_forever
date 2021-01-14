''' In order to import custom files from libraries folder,
 we need to reach libraries folder from source folder'''

import os
import sys
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.operation import add_num
from libraries.operation import sub_num
from libraries.operation import mul_num
from libraries.operation import div_num
from libraries.operation import odd_even
from libraries.helper import display_name
from libraries.helper import display_greeting
from libraries.leastchar import count_char
from libraries.osinformation import find_os_path_separator

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def oper_num():
    ''' In order to import custom files from libraries folder,
    we need to reach libraries folder from source folder'''
    display_greeting()
    name_2 = input("Please Enter Your name:")
    display_name(name_2)
    print("Now we are going to start Mathematical libraries.operations")
    value_1 = int(input("Please Enter a Number:"))
    value_2 = int(input("Please Enter another number:"))
    print(add_num(value_1,value_2))
    print(sub_num(value_1,value_2))
    print(mul_num(value_1,value_2))
    if value_2 == 0: # The condition will execute while second is zero
        value_2 = int(input("Please Enter a number other than zero:"))
    else:
        print(div_num(value_1,value_2))
    print(odd_even(value_2))
    my_str = input("Enter an string with spaces: ")
    print(count_char(my_str))
    print(find_os_path_separator())

if __name__ == '__main__':
    oper_num()
