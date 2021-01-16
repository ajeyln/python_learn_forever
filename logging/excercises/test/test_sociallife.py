# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
import pytest
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.sociallife import find_friend_surname
from libraries import sociallife
from libraries.sociallife import mod_info_dict, del_info_dict

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

def test_mod_info_dict(monkeypatch):
    "to check dictionary with values"
    monkeypatch.setitem(sociallife.PERSON_INFO, "Name", "Akash")
    monkeypatch.setitem(sociallife.PERSON_INFO, "Surname", "Sharma")
    expected_value = "Name=Akash; Surname=Sharma;"
    assert expected_value == mod_info_dict()

def test_missing_user(monkeypatch):
    "to check dictionary after deleting key values"
    monkeypatch.delitem(sociallife.PERSON_DET, "Name", raising=False)

    with pytest.raises(KeyError):
        _ = del_info_dict()
