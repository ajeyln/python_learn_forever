# The scripts is to find the operating system of curret machine

'''importing Libraries'''
import platform

def find_os(os_name):
    ''' conditions ro check operating system'''
    if os_name == "Windows" :
        print(f"The operating system of the current machine is {os_name}")
    else:
        print(f"The operating system of the current machine is {os_name}")

if __name__ == "__main__":
    oper_system = platform.system()
    find_os(oper_system)
