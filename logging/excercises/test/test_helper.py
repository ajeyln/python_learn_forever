# The Scripts is to test the helper.py

''' Set up for importing file'''
import os
import sys
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

filehandler_debug = logging.FileHandler("..\output\testhelper.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("..\output\testhelper.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("..\output\testhelper.log")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.helper import display_name
from libraries.helper import display_greeting, say_hello

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_display_name():
    ''' This test is check display name function'''
    user_name = "Ajeya"
    expected_value = "Your name is Ajeya"
    logger.debug(f"Input value is {user_name}")
    logger.debug(f"Expected value is {expected_value}")
    actual_value = display_name(user_name)
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == display_name(user_name)

def test_display_greeting():
    ''' This test is check display greeting function'''
    expected_value = "Welcome to India"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = display_greeting()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == display_greeting()

def test_base_file(capsys):
    "to check greetings"
    say_hello()
    out,err = capsys.readouterr()
    expected_value = "Hello World\n"
    logger.debug(f"Expected value is {out}")
    actual_value = out
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert out == expected_value
    assert err ==""
