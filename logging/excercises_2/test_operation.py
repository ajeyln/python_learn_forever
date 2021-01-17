# The Scripts is to test the operation.py

''' Set up for importing file'''
import pytest
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# file handler for Debug
formatter_debug = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_debug = logging.FileHandler('test_operation.log')
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

file_info = logging.FileHandler('test_operation.log')
file_info.setLevel(logging.INFO)
file_info.setFormatter(formatter_info)

logger.addHandler(file_info)

# file Handler Critical
formatter_critical = logging.Formatter('%(message)s:%(asctime)s:%(levelname)s')

file_critical = logging.FileHandler('test_operation.log')
file_critical.setLevel(logging.CRITICAL)
file_critical.setFormatter(formatter_critical)

logger.addHandler(file_critical)


#pylint: disable=wrong-import-position
#pylint: disable=import-error

from operation import add_num
from operation import sub_num
from operation import div_num
from operation import mul_num
from operation import odd_even

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_add_num():
    ''' to test add_num function in operation file'''
    logger.info("testing add_num function in operation file")
    num_1 = 4
    num_2 = 5
    logger.info(f"first values is {num_1}")
    logger.info(f"second values is {num_2}")
    expected_value = 9
    assert expected_value == add_num(num_1, num_2)

def test_sub_num():
    ''' to test sub_num function in operation file'''
    logger.info("testing sub_num function in operation file")
    num_1 = 12
    num_2 = 3
    logger.info(f"first values is {num_1}")
    logger.info(f"second values is {num_2}")
    expected_value = 9
    assert expected_value == sub_num(num_1, num_2)

def test_mul_num():
    ''' to test mul_num function in operation file'''
    try:
        mul_num(10, 8)
    except Exception as exc:
        pytest.fail(f"Test is failed due to {exc}")


@pytest.mark.parametrize("num_1, num_2, expected_value",[(9, 2, 4.5), (15, 0, None)])
def test_div_num(num_1, num_2, expected_value):
    ''' to test div_num function in operation file'''
    logger.info("testing div_num function in operation file")
    logger.info(f"first values is {num_1}")
    logger.info(f"second values is {num_2}")
    assert expected_value == div_num(num_1, num_2)

@pytest.mark.parametrize("num_1, expected_value",[(4, "even"),(7, "odd")])
def test_odd_even(num_1, expected_value):
    ''' to test odd_even function in operation file'''
    logger.info("Testing the number is odd or not")
    assert expected_value == odd_even(num_1)
