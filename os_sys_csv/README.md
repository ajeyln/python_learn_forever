<h1 align="Center"> File Operation</h1>

## Table of Content

* [Background](#background)
* [Content](#content)
    + [Creating folder](#create_folder)
    + [Converting list of dictionaries to csv](#csv_list_dict)
    + [List_dict_csv](#list_dict_csv)
    + [Generate Directory paths files, folders](#list_files)

## <a name="background"></a> Background <br />
File is defined as a set of related data or information. <br />
Folders help us to keep our files organized and separate and folder can have sub folders as well <br />

In this folder, we have created file and folder operation based on following modules 
1. **os** - The OS module in Python provides functions for interacting with the operating system.
OS comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality. <br />
2. **sys** - The python sys module provides functions and variables which are used to manipulate paths of the Python Runtime Environment. <br />
3. **csv** -  The csv library contains objects and other code to read, write, and process data from and to CSV files.

## <a name="content"></a>Content<br />
There are 4 sub-folders in os_sys_csv folder

### <a name="create_folder"></a>1. Creating folder <br >
In this folder, the script where used to generate folder, sub-folder and files.

+  create_folder.py - This script will generate text file from 1 to 49 and move these files to respective sub-folders which named based the file number dividing by 10
+ result - this is the resultant folder, currently there is no sub-folder files under this folder.(the sub-folder and files are generated after execution of the script create_folder.py)

### <a name="csv_list_dict"></a>2. Converting csv to list of dictionaries <br >
In this folder, the script where used to convert a .csv file to list of dictionaries.

+ csv_list_dict.py - The script will convert the .csv file to list of dictionaries.

### <a name="list_dict_csv"></a>3. Converting list of dictionaries to csv <br >
In this folder, the script where used to convert list of dictionaries to a .csv file.

+ list_dict_csv.py - The script will convert the list of dictionaries to a .csv file.

### <a name="list_files"></a> 4. Generate Directory paths files, folders <br />
In this folder, the script where used to generate a text file which has full path of file, folder and sub-folder of directory.

+ file_list.py - The script will generate full the path all files and folder, sub-folders of a directory and saved in a text file.

+ fullpath.txt - resultant text file, which has full path of file, folder and sub-folder of directory.
