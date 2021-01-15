# The Scripts is to test the libraries.operation.py

''' Set up for importing file'''
import os
import sys
import pytest
sys.path.append(os.getcwd())

#pylint: disable=wrong-import-position
#pylint: disable=import-error

from libraries.operation import add_num
from libraries.operation import sub_num
from libraries.operation import div_num
from libraries.operation import mul_num
from libraries.operation import odd_even

#pylint: enable=wrong-import-position
#pylint: enable=import-error

def test_add_num():
    ''' to test add_num function in libraries.operation file'''
    num_1 = 4
    num_2 = 5
    expected_value = 9
    assert expected_value == add_num(num_1, num_2)

def test_sub_num():
    ''' to test sub_num function in libraries.operation file'''
    num_3 = 12
    num_4 = 3
    expected_value = 9
    assert expected_value == sub_num(num_3, num_4)

def test_mul_num():
    ''' to test mul_num function in libraries.operation file'''
    try:
        num_1 = 10
        num_2 = 0
        expected_value = 0
        assert expected_value == mul_num(num_1, num_2)
    except: 
        pytest.fail("Fail Occured due to exception")

@pytest.mark.parametrize("num_7, num_8, expected_value",[(9, 2, 4.5), (15, 0, None)])
def test_div_num(num_7, num_8, expected_value):
    ''' to test div_num function in libraries.operation file'''
    assert expected_value == div_num(num_7, num_8)

@pytest.mark.parametrize("num_11, expected_value",[(4, "even"),(7, "odd")])
def test_odd_even(num_11, expected_value):
    ''' to test odd_even function in libraries.operation file'''
    assert expected_value == odd_even(num_11)
