# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.osinformation import find_os_path_separator

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_find_os_path_separator():
    ''' this function is test the os information'''
    sys_name ="Linux"
    expected_value = "/"
    assert expected_value == find_os_path_separator(sys_name)
