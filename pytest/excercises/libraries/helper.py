''' This script take you name as input and display your name'''

''' This function take your name as input and display your name along with your name is '''
def display_name(name1):
    return "Your name is {}".format(name1)

''' This function displays as welcome to India and will not take any inputs '''
def display_greeting():
    return "Welcome to India"

if __name__ == '__main__':
    a = input("Enter You name:")
    display_name(a)
    display_greeting()