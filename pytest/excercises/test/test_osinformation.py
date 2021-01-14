# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
import platform
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.osinformation import find_os_path_separator

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_find_os_path_separator(monkeypatch):
    ''' this function is to check the os information'''
    monkeypatch.setattr(platform, "system", lambda : "Linux")
    expected_value = "/"
    assert expected_value == find_os_path_separator()

    monkeypatch.setattr(platform, "system", lambda : "Windows")
    expected_value = "\\"
    assert expected_value == find_os_path_separator()
