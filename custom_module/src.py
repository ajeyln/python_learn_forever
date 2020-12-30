''' importing from customised file'''
from operation import add_num
from operation import sub_num
from operation import mul_num
from operation import div_num
from operation import odd_even
from helper import display_name
from helper import display_greeting

''' This function do the mathematical operations'''
def oper_num(m,n):
    add_num(m,n)
    sub_num(m,n)
    mul_num(m,n)
    div_num(m,n)
    odd_even(n)

'''This function will greets with your entered name'''
def greet_man(name2):
    display_greeting()
    display_name(name2)

if __name__ == '__main__':
    name3 = input("Please Enter Your name:")
    greet_man(name3)
    c = int(input("Please Enter a Number:"))
    d = int(input("Please Enter another number:"))
    while(d == 0): # The condition will execute while second is zero
        d = int(input("Please Enter a number other than zero:"))
    else:
        print(oper_num(c,d))
