<h1 align="center">Custom Module </h1>

## Introduction
Python modules can get access to code from another module by importing the file/function using import method. <br />
The import statement is the most common way of invoking the import machinery <br />

## Content

**There are two types of imports in Python** <br/>

a. **Absolute Import** <br />
	Absolute import involves full path(from the root folder to the desired module). An absolute import state that the resource to be imported using its full path from the root folder. <br />
	Eg: If the source file and libraries are the in folder, <br />
	we can import file <br />
```python
	from (foldername).(filename) import (functionname)
``` 
    Note: 
	source file - The file, from where we are calling another file/module<br />
	libraries - The file, from whom we are refering the file/function
	
b. **Relative Import** <br />
	A relative import specifies the resource to be imported relative to the current location. <br />
	A relative import depends on the current location as well as the location of the module, package, or object to be imported <br />
	Eg 1: <br />
```python
	# Acessing the function when some_module and current file in same folder.
	from .some_module import some_class
```
Eg 2:
```python
	    # Acessing the function when librarie and current file in different folder.
	    from ..some_package import some_function 
```
	Note: In Relative Import 
	.(Single Dot) means the current folder, where main file kept.
	..(Double Dot) mean the foldera above than current folder.
	some_module, some_packges are the file in libraries
	some_class,some_function are the functions of some_module,some_packages respectively
	
	
##  Excercises

**Based on the types of imports in Python,I have organized the files in following method** : <br />

 1. **Situation_1 - In this instnace, I have kept source file and libraries file in same folder.** <br />
 
   I have imported the functions in operation, helper file using absolute import method <br/>
   ```python
   # accessing function add_num, odd_even from operation and display_name from helper file.
   from operation import add_num
   from operation import odd_even
   from helper import display_name
   ```
   Note :
   main.py is current file or source file
   operation and helper files are libraries
   
 2. **Situation_2 - In this case, I have kept libraries in libraries folder and source file out side of the folder** <br />
   
   I have imported the functions in operation, helper file using absolute import method <br />
   ```python
   # accessing function sub_num, mul_num from operation and display_greeting from helper file.
	from libraries.operation import sub_num 
	from libraries.operation import mul_num
	from libraries.helper import display_greeting
   ```
   
 3. **Situation_3 - In this method,I have kept libraries files in libraries folder and source file in source folder** <br />
 
   I have imported the functions in operation, helper file using sys module and relative import method <br />
   
   ```python
   # importing sys module to access libraries folder
   import sys 
   temp_list = str(__file__).split("/") # spliting current folder path
   temp_join = "/".join(temp_list[:-1]) # rejoin the folder path excluding the file name
   # concatenate the file path with libraries file path.
   temp_con = (temp_join + "/../libraries") # Using ..(double dot) as libraries file folder is the above the current file folder
   sys.path.append(temp_con) # accessing libraries folder
   
   #accessing function add_num, odd_even from operation and display_name from helper file.
   from operation import add_num
   from operation import odd_even
   from helper import display_name
   ```

##  Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Sys path append module](https://www.youtube.com/watch?v=-aWN9FYfkFA&feature=youtu.be) | Tutorial to add file path
2| [Jupyter Installation](https://www.youtube.com/watch?v=5z5nALNandM&feature=youtu.be) | System path and Changing Module Paths
