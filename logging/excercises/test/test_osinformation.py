# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
import platform
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

filehandler_debug = logging.FileHandler("output\test_osinformation.log")
filehandler_debug.setLevel(logging.DEBUG)
filehandler_debug.setFormatter(formatter_debug)

logger.addHandler(filehandler_debug)

# formatter handler for info
formatter_info = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_info = logging.FileHandler("output\test_osinformation.log")
filehandler_info.setLevel(logging.INFO)
filehandler_info.setFormatter(formatter_info)

logger.addFilter(filehandler_info)

# File Handler for critical
formatter_critical = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

filehandler_critical = logging.FileHandler("output\test_osinformation.log")
filehandler_critical.setLevel(logging.CRITICAL)
filehandler_critical.setFormatter(formatter_critical)

logger.addHandler(filehandler_critical)


#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.osinformation import find_os_path_separator

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_find_os_path_separator(monkeypatch):
    ''' this function is to check the os information'''
    logger.info('this function is to check the os information')
    monkeypatch.setattr(platform, "system", lambda : "Linux")
    expected_value = "/"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_os_path_separator()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_os_path_separator()

def test_find_windows_path_separator(monkeypatch):
    ''' this function is to check the os information'''
    logger.info('this function is to check the os information')
    monkeypatch.setattr(platform, "system", lambda : "Windows")
    expected_value = "\\"
    logger.debug(f"Expected value is {expected_value}")
    actual_value = find_os_path_separator()
    logger.debug(f"Actual value is {actual_value}")
    if expected_value == actual_value:
        logger.info("Test Passed")
    else:
        logger.critical("Test Failed")
    assert expected_value == find_os_path_separator()
