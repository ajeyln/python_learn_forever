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

def oper_num(name_2, value_1, value_2, my_str):
    ''' In order to import custom files from libraries folder,
    we need to reach libraries folder from source folder'''
    display_greeting()
    display_name(name_2)
    print("Now we are going to start Mathematical libraries.operations")
    print(add_num(value_1,value_2))
    print(sub_num(value_1,value_2))
    print(mul_num(value_1,value_2))
    if value_2 == 0: # The condition will execute while second is zero
        print("Zero Division error")
    else:
        print(div_num(value_1,value_2))
    print(odd_even(value_2))
    print(count_char(my_str))
    print(find_os_path_separator())

if __name__ == '__main__':
    item_1 = sys.argv[1]
    item_2 = sys.argv[2]
    item_3 = sys.argv[3]
    item_4 = sys.argv[4]
    oper_num(item_1, item_2, item_3, item_4)
