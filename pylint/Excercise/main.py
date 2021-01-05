''' importing from customised file'''
from operation import add_num
from operation import sub_num
from operation import mul_num
from operation import div_num
from operation import odd_even
from helper import display_name
from helper import display_greeting

def oper_num():
    ''' This function will greets with your entered name and do the mathematical operations'''
    display_greeting()
    name_2 = input("Please Enter Your name:")
    display_name(name_2)
    print("Now we are going to start Mathematical Operations")
    value_1 = int(input("Please Enter a Number:"))
    value_2 = int(input("Please Enter another number:"))
    add_num(value_1,value_2)
    sub_num(value_1,value_2)
    mul_num(value_1,value_2)
    if value_2 == 0: # The condition will execute while second is zero
        value_2 = int(input("Please Enter a number other than zero:"))
    else:
        print(div_num(value_1,value_2))
    odd_even(value_2)


if __name__ == '__main__':
    oper_num()