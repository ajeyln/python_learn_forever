# The scripts is to find the operating system of curret machine

'''importing Libraries'''
import platform

def find_os_path_separator():
    ''' conditions ro check operating system'''
    os_name = platform.system()
    if os_name == "Windows" :
        return "\\"
    else:
        return "/"
