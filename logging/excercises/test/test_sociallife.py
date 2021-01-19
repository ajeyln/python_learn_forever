# The Scripts is to test the osinformation.py

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

filehandler_debug = logging.FileHandler("output\test_sociallife.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\test_sociallife.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\test_sociallife.log")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.sociallife import find_friend_surname
from libraries import sociallife
from libraries.sociallife import mod_info_dict, del_info_dict

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_find_friend_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    logger.info('to find the friends surname in dict')
    monkeypatch.setattr('builtins.input', lambda prompt="":"Bharat")
    expected_value = "Pai"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_friend_surname()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_friend_surname()

def test_friend_invalid_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    logger.info('to find the friends surname in dict')
    monkeypatch.setattr('builtins.input', lambda prompt="":"Manoj")
    expected_value = False
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_friend_surname()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_friend_surname()

def test_mod_info_dict(monkeypatch):
    "to check dictionary with values"
    monkeypatch.setitem(sociallife.PERSON_INFO, "Name", "Akash")
    monkeypatch.setitem(sociallife.PERSON_INFO, "Surname", "Sharma")
    expected_value = "Name=Akash; Surname=Sharma;"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = mod_info_dict()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.debug("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == mod_info_dict()

def test_missing_user(monkeypatch):
    "to check dictionary after deleting key values"
    monkeypatch.delitem(sociallife.PERSON_DET, "Name", raising=False)

    with pytest.raises(KeyError):
        _ = del_info_dict()
