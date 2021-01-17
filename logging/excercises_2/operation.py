'''This script will do different mathematical operations such as addition, 
Substraction,Multiplication, division of two integers 
and also it shows, whether first number is odd or even'''
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# file handler for Debug
formatter_debug = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_debug = logging.FileHandler('operation.log')
file_debug.setLevel(logging.DEBUG)
file_debug.setFormatter(formatter_debug)

logger.addHandler(file_debug)

# Stream handler
formatter_stream = logging.Formatter('%(pathname)s:%(module)s:%(message)s')

stream_data = logging.StreamHandler()
stream_data.setFormatter(formatter_stream)

logger.addHandler(stream_data)

# file handler for Info
formatter_info = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_info = logging.FileHandler('operation.log')
file_info.setLevel(logging.INFO)
file_info.setFormatter(formatter_info)

logger.addHandler(file_info)

# file Handler Critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

file_critical = logging.FileHandler('operation.log')
file_critical.setLevel(logging.CRITICAL)
file_critical.setFormatter(formatter_critical)

logger.addHandler(file_critical)

def add_num(val_1,val_2):
    '''This function will add two integer numbers'''
    logger.info("Now we are in addition operation")
    temp = val_1 + val_2 
    logger.debug(f"The Value after addition is {temp}")
    return temp

def sub_num(val_1,val_2):
    '''This function will subtract two integer numbers'''
    logger.info("Now we are in subtract operation")
    temp = val_1 - val_2
    logger.debug(f"The Value after subteaction is {temp}")
    return temp

def mul_num(val_1,val_2):
    '''This function will multiply two integer numbers'''
    logger.info("Now we are in multiplication operation")
    temp = val_1 * val_2
    logger.debug(f"The Value after multiplication is {temp}")
    return temp

def div_num(val_1,val_2):
    '''This function will divide two integer numbers'''
    logger.info("Now we are in division operation")
    if val_2 == 0 : # The condition will execute while second is zero
        logger.debug("Zero Exception error")
        return None
    else:
        temp = val_1 / val_2
        logger.debug(f"The Value after multiplication is {temp}")
        return temp

def odd_even(val_1):
    '''This function will check the given number is even or odd'''
    logger.info("to check the number odd or even")
    if(val_1 % 2 == 0):
        logger.info(f"{val_1} is even")
        return "even"
    else:
        logger.info(f"{val_1} is odd")
        return "odd"
