''' In order to import custom files from libraries folder,
 we need to reach libraries folder from source folder'''

import os
import sys
sys.path.append(os.getcwd())
import logging

logging.basicConfig(filename='main.log', level=logging.INFO,
                format='%(asctime)s:%(name)s:%(message)s')

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
    logging.critical(f"The user name is {name_2}")
    logging.critical(f"The first number is {value_1}")
    logging.critical(f"The second number is {value_2}")
    logging.critical(f"The string name is {my_str}")
    display_greeting()
    display_name(name_2)
    x = add_num(value_1,value_2)
    logging.info(f"addition of two number is {x}")
    y = sub_num(value_1,value_2)
    logging.info(f"substraction of two number is {y}")
    z = mul_num(value_1,value_2)
    logging.info(f"Multiplication of two number is {z}")
    if value_2 == 0: # The condition will execute while second is zero
        logging.info("Zero Division error")
    else:
        logging.info(div_num(value_1,value_2))
    logging.info(odd_even(value_2))
    logging.info(find_os_path_separator())

if __name__ == '__main__':
    logging.info("Now we are doing mathematical operations")
    if len(sys.argv) != 5:
        print("$ python source\main.py <user_name> <number_1> <number_2> <string_name> ")
        sys.exit(1)
    
    user_name = str(sys.argv[1])
    number_1 = int(sys.argv[2])
    number_2 = int(sys.argv[3])
    string_name = str(sys.argv[4])
    oper_num(user_name, number_1, number_2, string_name)
