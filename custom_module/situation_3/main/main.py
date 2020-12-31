''' importing from customised file'''
from operation import add_num
from operation import sub_num
from operation import mul_num
from operation import div_num
from operation import odd_even
from helper import display_name
from helper import display_greeting

''' This function will greets with your entered name and do the mathematical operations'''
def oper_num(name_2, value_1, value_2):
    display_greeting()
    display_name(name_2)
    add_num(value_1,value_2)
    sub_num(value_1,value_2)
    mul_num(value_1,value_2)
    while(value_2 == 0): # The condition will execute while second is zero
        value_2 = int(input("Please Enter a number other than zero:"))
    else:
        print(div_num(value_1,value_2))
    odd_even(value_2)


if __name__ == '__main__':
    name_2 = input("Please Enter Your name:")
    value_1 = int(input("Please Enter a Number:"))
    value_2 = int(input("Please Enter another number:"))
    oper_num(name_2, value_1,value_2)
