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

if __name__ == "__main__":
    path_separator = find_os_path_separator()
    print(path_separator)
