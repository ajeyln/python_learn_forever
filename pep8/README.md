<h1 align="center">Python Enhancement Purposal </h1>

## Introduction

**PEP8** is a document that provides guidelines and best practices on how to write Python code.<br />
This document gives coding conventions for the Python code comprising the standard library in the main Python distribution <br />

* **Naming Convesion**

 + **Regular Variable**
	Variable Name Should be lowercase, where necessary separating words by underscope <br />
	Eg:
	```python 
	owner_name = 'Srinivas'
	```
	
 + **CONSTANTS**
	- In python, all variable can be modified, Therefore real constants don't exist<br />
	- If we want to make any varibale constant, name should be uppercase, where necessary separating words by underscore<br />
	Eg:
	```python
	INDIAN_CAPITAL = 'New Delhi'
	```
+ **function name()**
	- Names of functions and class method should be lowercase, where necessary separating word by underscore.<br />
	Eg:
	```python
	import random
	
	def add_numbers(a,b):
		temp = a
		sum = temp + b
		return sum
		
	if name = "main()":
		x = random.randint(0,100)
		y = random.randint(1,50)
	
		total = add_number(x,y)
		print(total)
	```

+ **Class Name**
	- Class Name Should be Capitalize the first letter of each word <br />
	Eg:
	```python
	Class India:
		
		def  __init__(self, state_name):
			self.name = state_name
		
		def __str__(self):
			return self.name
		
	karnataka = India(state_name = 'Karnataka')
	print(karnataka)
	```
	
+ **FactoryFunctionNames()** <br />
	- Factory functions returns objects, therefore to user of our code, factory function as class definition <br />
	- To reflect this, the factory function name should also capitalize the first letter of each word <br />
	
	```python
	def Maharastra():
		return India(state_name = 'Maharastra')
		
	name = Maharastra()
	print(name)
	```
	
* **Identation** - Use 4 spaces per indentation level.<br />
Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent <br />
	
	# Aligned with opening delimiter.<br />
    ```python
	foo = long_function_name(var_one, var_two,
                         var_three, var_four)
	```

	# More indentation included to distinguish this from the rest.<br />
	```python
	def long_function_name(
			var_one, var_two, var_three,
			var_four):
		print(var_one)
	```

	# Hanging indents should add a level.<br />
	```python
	foo = long_function_name(
		var_one, var_two,
    var_three, var_four)
	```
	
  * when the conditional part of an if statement, no extra indentation required<br />
	# No extra indentation.<br />
	```python
	if (this_is_one_thing and
		that_is_another_thing):
		do_something()
	```

  * Add a comment, Which will provide some information in editor <br />
	```python
	if (this_is_one_thing and
		that_is_another_thing): # Since both conditions are true, we can frobnicate.
		do_something()
	```

  * The closing brace/bracket/parenthesis on multi-line constructs may either line up under the first non-whitespace character of the last line of list, <br />
	```python
	my_list = [
		1, 2, 3,
		4, 5, 6,
		]
	```
	or
	```python
	my_list = [
		1, 2, 3,
		4, 5, 6,
	]
	```
	
* **Maximum Line Length** - Limit all lines to a maximum of 79 characters. <br />
	The preferred way of wrapping long lines is by using Python’s implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses. <br />
	These should be used in preference to using a backslash for line continuation.<br />

	Backslashes may still be appropriate at times. For example, long, multiple with-statements cannot use implicit continuation, so backslashes are acceptable: <br />
	```python
	with open('/path/to/some/file/you/want/to/read') as file_1, \
		open('/path/to/some/file/being/written', 'w') as file_2:
		file_2.write(file_1.read())
	```

* Line break before or after a binary operator?<br />
	It is permissible to break before or after a binary operator, as long as the convention is consistent locally.
	
	Following the tradition from mathematics usually results in more readable code: <br />	
	```python
	income = (gross_wages
			+ taxable_interest
			+ (dividends - qualified_dividends)
			- ira_deduction
			- student_loan_interest)
	```
	
* **Imports**<br />
	Imports should usually be on separate lines
	
	```python
	import os
	import sys
	```
	
	Also, The followings are acceptable:<br />
	```python
	from subprocess import Popen, PIPE
	```

* **Whitespace in Expressions and Statements**<br />
Avoid extraneous whitespace in the following situations:<br />
	
	+ Immediately inside parentheses, brackets or braces:
	
	**Should be**<br />
	```python
	spam(ham[1], {eggs: 2}) 
	```
	
	**Should not be**<br />
	```python
	spam( ham[ 1 ], { eggs: 2 } )
	```
	
	+ Between a trailing comma and a following close parenthesis:

	**Should be**<br />
	```python
	foo = (0,)
	```
	
	**Should not be**<br />
	```python
	bar = (0, )
	```
	
	+ Immediately before a comma, semicolon, or colon:
	
	**Should be**<br />
	```python
	if x == 4: print x, y; x, y = y, x
	```

	**Should not be**<br />
	```python
	if x == 4 : print x , y ; x , y = y , x
	```

* **When to use trailing commas**<br />

	when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line. <br />
	
	**Should be**<br />
	```python
	FILES = [
		'setup.cfg',
		'tox.ini',
		]
	initialize(FILES,
           error=True,
           )
	```
	
	**Should not be**<br />
	```python
	FILES = ['setup.cfg', 'tox.ini',]
	initialize(FILES, error=True,)
	```
##  Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------------------------------------------------------------------------------|
1| https://pep8.org/ | PEP8 Style Guide for Python code |
2| https://www.youtube.com/watch?v=Sm0wwmEwqpI&fbclid=IwAR1Q78KGJyPS1arHwc0NGT6LFX1mYiZ54Km5jFhaAyCM6PCQXLnhcTr_F6g%29 | PEP8 Naming Convention|
