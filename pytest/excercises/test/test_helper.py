# The Scripts is to test the helper.py

''' Set up for importing file'''
import os
import sys
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.helper import display_name
from libraries.helper import display_greeting

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_display_name():
    ''' This test is check display name function'''
    user_name = "Ajeya"
    expected_value = "Your name is Ajeya"
    assert expected_value == display_name(user_name)

def test_display_greeting():
    ''' This test is check display greeting function'''
    expected_value = "Welcome to India"
    assert expected_value == display_greeting()
