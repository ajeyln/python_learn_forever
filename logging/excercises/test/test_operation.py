# The Scripts is to test the libraries.operation.py

''' Set up for importing file'''
import os
import sys
import pytest
import logging
sys.path.append(os.getcwd())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#log creation for stream
fomatter_stream = logging.Formatter('%(pathname)s:%(asctime)s:%(message)s')

stream_data = logging.StreamHandler()
stream_data.setFormatter(fomatter_stream)

logger.addHandler(stream_data)

# File handler for debug
formatter_debug = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_debug = logging.FileHandler("output\test_operation.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\test_operation.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\test_operation.log")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.operation import add_num
from libraries.operation import sub_num
from libraries.operation import div_num
from libraries.operation import mul_num
from libraries.operation import odd_even

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_add_num():
    ''' to test add_num function in libraries.operation file'''
    logger.info('test to add two integer')
    num_1 = 4
    num_2 = 5
    logger.debug(f"Input value 1 is {num_1}")
    logger.debug(f"Input value 1 is {num_2}")
    expected_value = 9
    logger.debug(f"Expected value is {expected_value}")
    actual_value = add_num(num_1, num_2)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == add_num(num_1, num_2)

def test_sub_num():
    ''' to test sub_num function in libraries.operation file'''
    logger.info('test to subtract two integer')
    num_3 = 12
    num_4 = 3
    logger.debug(f"Input value 1 is {num_3}")
    logger.debug(f"Input value 1 is {num_4}")
    expected_value = 9
    logger.debug(f"Expected value is {expected_value}")
    actual_value = sub_num(num_3, num_4)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == sub_num(num_3, num_4)

def test_mul_num():
    ''' to test mul_num function in libraries.operation file'''
    try:
        mul_num(10, 8)
    except Exception as exc:
        pytest.fail(f"Test is failed due to {exc}")


@pytest.mark.parametrize("num_7, num_8, expected_value",[(9, 2, 4.5), (15, 0, None)])
def test_div_num(num_7, num_8, expected_value):
    ''' to test div_num function in libraries.operation file'''
    logger.info(' test to check division of two numbers ')
    logger.debug(f"Input value 1 is {num_7}")
    logger.debug(f"Input value 1 is {num_8}")
    logger.debug(f"Expected value is {expected_value}")
    actual_value = div_num(num_7, num_8)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == div_num(num_7, num_8)

@pytest.mark.parametrize("num_11, expected_value",[(4, "even"),(7, "odd")])
def test_odd_even(num_11, expected_value):
    ''' to test odd_even function in libraries.operation file'''
    logger.info(' test to check whether number is odd or even')
    logger.debug(f"Input value 1 is {num_11}")
    logger.debug(f"Expected value is {expected_value}")
    actual_value = odd_even(num_11)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == odd_even(num_11)
