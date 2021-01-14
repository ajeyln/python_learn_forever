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
    def find_os():
        return "Linux"
    monkeypatch.setattr(platform, "system", find_os)
    expected_value = "/"
    assert expected_value == find_os_path_separator()

    def find_windows_os():
        return "Windows"
    monkeypatch.setattr(platform, "system", find_windows_os)
    expected_value = "\\"
    assert expected_value == find_os_path_separator()
