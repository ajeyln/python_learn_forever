''' The script is '''
def add_num(a,b):
    return a + b

def sub_num(a,b):
    return a - b

def mul_num(a,b):
    return a * b

def div_num(a,b):
    return a/ b

def odd_even(a):
    if(a % 2 == 0):
        print("{0} is even". format(a))
    else:
        print("{0} is odd". format(a))

if __name__ == "__main__":
    x = int(input("Please Enter a Number:"))
    y = int(input("Please Enter another number:"))
    print(add_num(x,y))
    print(sub_num(x,y))
    print(mul_num(x,y))
    while(y == 0):
        y = int(input("Please Enter a number other than zero:"))
    else:
        print(div_num(x,y))
    odd_even(x)

