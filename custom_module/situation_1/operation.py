'''This script will do different mathematical operations such as addition, 
Substraction,Multiplication, division of two integers 
and also it shows, whether first number is odd or even'''

'''This function will add two integer numbers'''
def add_num(a,b):
    temp = a + b 
    print("The Value after subtracting two given numbers: {}".format(temp))

'''This function will subtract two integer numbers'''
def sub_num(a,b):
    temp = a - b
    print("The Value after subtracting two given numbers: {}".format(temp))

'''This function will multiply two integer numbers'''
def mul_num(a,b):
    temp = a * b
    print("The Value after multiplying two given numbers: {}".format(temp))

'''This function will divide two integer numbers'''
def div_num(a,b):
    while(b == 0): # The condition will execute while second is zero
        b = int(input("Please Enter a number other than zero:"))
    else:
        temp = a / b
        print("The Value after division: {}".format(temp))

'''This function will check the given number is even or odd'''
def odd_even(a):
    if(a % 2 == 0):
        print("{0} is even". format(a))
    else:
        print("{0} is odd". format(a))

if __name__ == "__main__":
    x = int(input("Please Enter a Number:"))
    y = int(input("Please Enter another number:"))
    add_num(x,y)
    sub_num(x,y)
    mul_num(x,y)
    div_num(x,y)
    odd_even(x)

