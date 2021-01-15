# The Scripts is to test the osinformation.py

''' Set up for importing file'''
import os
import sys
from io import StringIO

sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.sociallife import find_friend, find_friend_surname

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_find_friend(monkeypatch):
    ''' to check the friend name is in list or not'''
    friend_name = StringIO('Vikas\n')
    monkeypatch.setattr('sys.stdin', friend_name)
    assert False == friend_name()

def test_find_friend_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    friend_surname = StringIO('Puneet\n')
    monkeypatch.setattr('sys.stdin', friend_surname)
    assert 'Kumar' == find_friend_surname()

