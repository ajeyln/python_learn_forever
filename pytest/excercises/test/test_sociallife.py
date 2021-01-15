# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.sociallife import find_friend_surname

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_find_friend_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    monkeypatch.setattr('builtins.input', lambda prompt="":"Bharat")
    expected_value = "Pai"
    assert expected_value == find_friend_surname()

def test_friend_invalid_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    monkeypatch.setattr('builtins.input', lambda prompt="":"Manoj")
    expected_value = False
    assert expected_value == find_friend_surname()
