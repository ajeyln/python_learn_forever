'''This script will do different mathematical operations such as addition, 
Substraction,Multiplication, division of two integers 
and also it shows, whether first number is odd or even'''

'''This function will add two integer numbers'''
def add_num(a,b):
    temp = a + b 
    return temp

'''This function will subtract two integer numbers'''
def sub_num(a,b):
    temp = a - b
    return temp

'''This function will multiply two integer numbers'''
def mul_num(a,b):
    temp = a * b
    return temp

'''This function will divide two integer numbers'''
def div_num(a,b):
    if b == 0 : # The condition will execute while second is zero
        return None
    else:
        temp = a / b
        return temp

'''This function will check the given number is even or odd'''
def odd_even(a):
    if(a % 2 == 0):
        return "even"
    else:
        return "odd"
