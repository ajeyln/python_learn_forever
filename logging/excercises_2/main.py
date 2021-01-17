''' In order to import custom file operation.py and to do mathematical operation'''
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# file handler for Debug
formatter_debug = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler_debug = logging.FileHandler('main.log')
file_handler_debug.setLevel(logging.DEBUG)
file_handler_debug.setFormatter(formatter_debug)

logger.addHandler(file_handler_debug)

# Stream handler
stream_data = logging.StreamHandler()
stream_data.setFormatter(formatter_debug)

logger.addHandler(stream_data)

# file handler for Info
formatter_info = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s')

file_handler_info = logging.FileHandler('main.log')
file_handler_info.setLevel(logging.INFO)
file_handler_info.setFormatter(formatter_info)

logger.addHandler(file_handler_info)

# file Handler Critical
formatter_critical = logging.Formatter('%(asctime)s:%(message)s:%(name)s')

file_handler_critical = logging.FileHandler('main.log')
file_handler_critical.setLevel(logging.CRITICAL)
file_handler_critical.setFormatter(formatter_critical)

logger.addHandler(file_handler_critical)

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from operation import add_num
from operation import sub_num
from operation import mul_num
from operation import div_num
from operation import odd_even

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def oper_num(value_1, value_2):
    ''' In order to import custom files from libraries folder,
    we need to reach libraries folder from source folder'''
    logger.critical(f"The first number is {value_1}")
    logger.critical(f"The second number is {value_2}")
    x = add_num(value_1,value_2)
    logger.info(f"addition of two number is {x}")
    y = sub_num(value_1,value_2)
    logger.info(f"substraction of two number is {y}")
    z = mul_num(value_1,value_2)
    logger.info(f"Multiplication of two number is {z}")
    if value_2 == 0: # The condition will execute while second is zero
        logger.debug("Zero Division error")
    else:
        a1 = div_num(value_1,value_2)
        logger.debug(a1)
    logger.info(odd_even(value_2))

if __name__ == '__main__':
    logger.info("Now we are doing mathematical operations")
    if len(sys.argv) != 3:
        print("$ python main.py <number_1> <number_2> ")
        sys.exit(1)
    
    number_1 = int(sys.argv[1])
    number_2 = int(sys.argv[2])
    logger.info(f"Command line argument is {sys.argv}")
    oper_num(number_1, number_2)
