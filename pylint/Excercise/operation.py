'''This script will do different mathematical operations such as addition,
Substraction,Multiplication, division of two integers
and also it shows, whether first number is odd or even'''

def add_num(num_1,num_2):
    '''This function will add two integer numbers'''
    temp = num_1 + num_2
    print("The Value after subtracting two given numbers: {}".format(temp))

def sub_num(num_1,num_2):
    '''This function will subtract two integer numbers'''
    temp = num_1 - num_2
    print("The Value after subtracting two given numbers: {}".format(temp))

def mul_num(num_1,num_2):
    '''This function will multiply two integer numbers'''
    temp = num_1 * num_2
    print("The Value after multiplying two given numbers: {}".format(temp))

def div_num(num_1,num_2):
    '''This function will divide two integer numbers'''
    if num_2 == 0: #The condition will execute while second is zero
        num_2 = int(input("Please Enter a number other than zero:"))
    else:
        temp = num_1 / num_2
    print("The Value after division: {}".format(temp))

def odd_even(num_1):
    '''This function will check the given number is even or odd'''
    if num_1 % 2 == 0:
        print("{0} is even". format(num_1))
    else:
        print("{0} is odd". format(num_1))

if __name__ == "__main__":
    int_1 = int(input("Please Enter a Number:"))
    int_2 = int(input("Please Enter another number:"))
    add_num(int_1,int_2)
    sub_num(int_1,int_2)
    mul_num(int_1,int_2)
    div_num(int_1,int_2)
    odd_even(int_1)
    