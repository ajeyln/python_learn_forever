<h1 align="Center"> Pylint</h1>

## Introduction
   + Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard. <br>
   + It can also look for certain type errors and recommend suggestions about how particular blocks can be refactored. <br />
   + The code is given an overall mark, based on the number and severity of the warnings and errors.

## Content

### **Installation**
   
+ Pylint can be easily installed using pip  install <br />
``` pip install pylint ```

### **Running Pylint**
+ Pylint can be runned from the command line and usage is <br />
```pylint module/package or directory/module.py ```

### **Pylint Output**
+ The default format for the output is text and message format is <br />
``` MESSAGE_TYPE: LINE_NUM:[OBJECT:] MESSAGE ``` <br />
There are 5 kind of message types :
  * (C) convention, for programming standard violation
  * (R) refactor, for bad code smell
  * (W) warning, for python specific problems
  * (E) error, for much probably bugs in the code
  * (F) fatal, if an error occurred which prevented pylint from doing
  further processing.

#### **Naming Styles**
+ By default Pylint will enforce **PEP8** suggested names <br />
+ Pylint also recognizes a number of different name types internally with a few exceptions <br /> 

|Name Type|Description|
|---------|-----------|
|module	|Module and package names, same as the file names.|
|const|	Module-level constants, any variable defined at module level that is not bound to a class object.|
|class|	Names in class statements, as well as names bound to class objects at module level.|
|function	|Functions, toplevel or nested in functions or methods.|
|method|	Methods, functions defined in class bodies. Includes static and class methods.|
|attr|	Attributes created on class instances inside methods.|
|argument|	Arguments to any function type, including lambdas.|
|variable	|Local variables in function scopes.|
|class-attribute|	Attributes defined in class bodies.|
|inlinevar	|Loop variables in list comprehensions and generator expressions.| 
<br />

+ Pylint provides set of predefined naming styles. Those predefined naming styles may be used to adjust Pylint configuration

    Following predefined naming styles are available: <br />
    - snake_case <br />
    - camelCase <br />
    - PascalCase <br />
    - UPPER_CASE <br />
    - any - fake style which does not enforce any limitations

### **Most common error while running Pylint**

+ Error : **inconsistent use of tabs and spaces** <br />
This is the common error in if/else statement. These error message getting due to more or less spaces during identation. These can be solved by replacing with four spaces <br />

+ Error: **Line too long (106/100) (line-too-long)** <br />
This error will get if the line length very long, so need to separate the rest onto a newline <br />

+ Error: **Trailing whitespace (trailing-whitespace)** <br />
This error is due extra while spaces and can be solved by deleting those white spaces <br />

+ Error: **Missing module docstring (missing-docstring)**
This message is because there isn't a docstring in python script. This can be solved by writing docstring.

##  Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Pylint Tuorial](https://www.youtube.com/watch?v=C-gEQdGVXbk)| Pylint Tutorial |
2|[Pylint Tutorial Guide](https://docs.pylint.org/en/1.6.0/tutorial.html) | Begginer's Guide for Pylint |

 
