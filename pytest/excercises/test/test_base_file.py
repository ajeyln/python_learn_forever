# The Scripts is to test the base_file

''' Set up for importing file'''
import os
import sys
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.base_file import say_hello

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_base_file(capsys):
    "to check greetings"
    say_hello()
    out,err = capsys.readouterr()
    expected_value = "Hello World\n"
    assert out == expected_value
    assert err ==""