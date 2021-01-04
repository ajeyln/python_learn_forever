<h1 align="center">Custom Module </h1>

## Introduction
Python modules can get access to code from another module by importing the file/function using import method. <br />
The import statement is the most common way of invoking the import machinery <br />

### There are mainly two types of imports in Python

a. **Absolute Import** <br />
	Absolute import involves full path(from the root folder to the desired module). An absolute import state that the resource to be imported using its full path from the root folder. <br />
	Eg: If the source file and libraries are the in folder, 
	we can import file
	```python
	from (foldername).(filename) import (functionname)
	```
	* source file - The file, from where we are calling another file/module<br />
	* libraries - The file, from whom we are refering the file/function
	
b. **Relative Import** <br />
	A relative import specifies the resource to be imported relative to the current location. <br />
	A relative import depends on the current location as well as the location of the module, package, or object to be imported <br />
	Eg: here are some examples
	```python
	from .some_module import some_class # Here library(some_module)is in same folder as source file and we are trying to access function called some_class
	from ..some_package import some_function # Here library(some_module)is in another folder than source file and we are traing to access function called some_function
	```
	Note: In Relative Import <br />
	.(Single Dot) means the current folder, where main file kept.<br />
	..(Double Dot) mean the foldera above than current folder.
	
#### Based on the above type of imports in Python, I have kept the files in 3 different method as follows: <br />

   1. **Situation_1** <br /> 
   In this instnace, we kept source file(main.py) and libraries(operation.py and helper.py) in same file and trying to import source file from main file <br />
   we have imported the file using absolute import in this way
   '''python
   #### I wanted to access function add_num, odd_even from operation and display_name from helper file.
   from operation import add_num
   from operation import odd_even
   from helper import display_name
   '''
   
   2. **Situation_2** <br />
   In this case, we kept libraries(operation.py and helper.py) in libraries folder and source file(main.py)out side and want to import source file from main file <br />
   we have imported the file using absolute path in this way
   '''python
   #### I wanted to access function sub_num, mul_num from operation and display_greeting from helper file.
	from libraries.operation import sub_num # as the fource file in libraries we need to start from libraries folder to acces function
	from libraries.operation import mul_num
	from libraries.helper import display_greeting
   '''
   
   3. **Situation_3** <br />
   In this method, we kept libraries(operation.py and helper.py) in libraries folder and source file(main.py) in source folder and want to import source file from main file <br />
   we have imported the file in this way
   '''python
   #### we want to access libraries folder path, so we are importing sys module
   import sys 
   temp_list = str(__file__).split("/") # we are spliting current folder path
   temp_join = "/".join(temp_list[:-1]) # we need to execlude current file from path
   temp_con = (temp_join + "/../libraries") # we need to add libraries path to current file path excluding the current working file.
   ##### as libraries file folder is the above the current file folder we need to use ..(double dot)
   sys.path.append(temp_con
   #### I wanted to access function add_num, odd_even from operation and display_name from helper file.
   from operation import add_num
   from operation import odd_even
   from helper import display_name
   '''

##  Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Sys path append module](https://www.youtube.com/watch?v=-aWN9FYfkFA&feature=youtu.be) | Tutorial to add file path
2| [Jupyter Installation](https://www.youtube.com/watch?v=5z5nALNandM&feature=youtu.be) | System path and Changing Module Paths
