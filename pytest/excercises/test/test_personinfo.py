# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
import pytest
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries import personinfo
from libraries.personinfo import mod_info_dict, del_info_dict

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_mod_info_dict(monkeypatch):
    "to check dictionary with values"
    monkeypatch.setitem(personinfo.PERSON_INFO, "Name", "Akash")
    monkeypatch.setitem(personinfo.PERSON_INFO, "Surname", "Sharma")
    expected_value = "Name=Akash; Surname=Sharma;"
    assert expected_value == mod_info_dict()

def test_missing_user(monkeypatch):
    "to check dictionary after deleting key values"
    monkeypatch.delitem(personinfo.PERSON_DET, "Name", raising=False)

    with pytest.raises(KeyError):
        _ = del_info_dict()
