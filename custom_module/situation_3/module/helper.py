''' This script take you name as input and display your name'''

''' This function take your name as input and display your name along with your name is '''
def display_name(name1):
    print("Your name is {}".format(name1))

''' This function displays as welcome to India and will not take any input '''
def display_greeting():
    print("Welcome to India")

if __name__ == '__main__':
    a = input("Enter You name:")
    display_name(a)
    display_greeting()